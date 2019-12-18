from django.shortcuts import render
from rooms import models

def save_room(request):
    room = models.Room.objects.get_or_none(pk=pk)
    if room is not None:
        