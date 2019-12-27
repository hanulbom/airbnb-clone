import datetime
from django.http import Http404
from django.views.generic import View, ListView
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from rooms import models as room_models
from users import models as user_models
from reviews import forms as review_forms
from django.views.generic import TemplateView
from . import models


class CreateError(Exception):
    pass


def create(request, room, year, month, day):
    try:
        date_obj = datetime.datetime(year, month, day)
        room = room_models.Room.objects.get(pk=room)
        models.BookedDay.objects.get(day=date_obj, reservation__room=room)
        raise CreateError()
    except (room_models.Room.DoesNotExist, CreateError):
        messages.error(request, "Can't Reserve That Room")
        return redirect(reverse("core:home"))
    except models.BookedDay.DoesNotExist:
        reservation = models.Reservation.objects.create(
            guest=request.user,
            room=room,
            check_in=date_obj,
            check_out=date_obj + datetime.timedelta(days=1),
        )
        return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class ReservationDetailView(View):
    def get(self, *args, **kwargs):
        pk = kwargs.get("pk")
        reservation = models.Reservation.objects.get_or_none(pk=pk)
        if not reservation or (
            reservation.guest != self.request.user
            and reservation.room.host != self.request.user
        ):
            raise Http404()
        form = review_forms.CreateReviewForm()
        return render(
            self.request,
            "reservations/detail.html",
            {"reservation": reservation, "form": form},
        )


def edit_reservation(request, pk, verb):
    reservation = models.Reservation.objects.get_or_none(pk=pk)
    if not reservation or (
        reservation.guest != request.user and reservation.room.host != request.user
    ):
        raise Http404()
    if verb == "confirm":
        reservation.status = models.Reservation.STATUS_CONFIRMED
    elif verb == "cancel":
        reservation.status = models.Reservation.STATUS_CANCELED
        models.BookedDay.objects.filter(reservation=reservation).delete()
    reservation.save()
    messages.success(request, "Reservation Updated")
    return redirect(reverse("reservations:detail", kwargs={"pk": reservation.pk}))


class SeeReservationsView(ListView):

    """ See Reservations View Definition """

    user = user_models.User
    template_name = "reservations/see_reservations.html"

    def get(self, *args, **kwargs):
        user = self.request.user
        reservations = models.Reservation.objects.filter(guest__pk=user.pk)
        if not reservations.count() == 0:
            return render(
                self.request,
                "reservations/see_reservations.html",
                context={
                    "reservations": reservations,
                    "exist": True,
                    "cur_page": "reservations",
                },
            )
        else:
            return render(
                self.request,
                "reservations/see_reservations.html",
                context={"exist": False, "cur_page": "reservations"},
            )


class SeeHostRoomsReservations(ListView):

    """ See Host Rooms Reservations View Definition """

    model = user_models.User
    template_name = "reservations/see_reservations.html"

    def get(self, *args, **kwargs):
        host = self.request.user
        reservations = models.Reservation.objects.filter(
            room__host__pk=host.pk
        )
        if not reservations.count() == 0:
            return render(
                self.request,
                "reservations/see_reservations.html",
                context={
                    "reservations": reservations,
                    "exist": True,
                    "cur_page": "reservations-host",
                },
            )
        else:
            return render(
                self.request,
                "reservations/see_reservations.html",
                context={"exist": False, "cur_page": "reservations-host"},
            )