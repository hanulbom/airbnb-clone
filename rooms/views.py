from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def all_rooms(request):
    return render(request, "all_rooms")
