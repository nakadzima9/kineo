from django.contrib import admin
from .models import Cinema, MovieFormat, Room, RoomFormat, Seat, ShowTime

admin.site.register((Cinema, MovieFormat, Room, RoomFormat, Seat, ShowTime))
