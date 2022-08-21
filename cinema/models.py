from django.db import models
from movie.models import Movie


class Cinema(models.Model):
    cinema_title = models.CharField(max_length=255, verbose_name="Название кинотеатра")
    cinema_description = models.TextField(verbose_name="Описание кинотеатра")
    cinema_startTime = models.DateTimeField(auto_now_add=True)
    cinema_endTime = models.DateTimeField(auto_now_add=True)
    cinema_address = models.CharField(max_length=255, verbose_name="Адрес кинотеатра")
    cinema_website = models.URLField(max_length=200, null=True, blank=True, verbose_name="Сайт кинотеатра")

    def __str__(self):
        return self.cinema_title


class Room(models.Model):
    room_name = models.CharField(max_length=50, verbose_name="Зал")
    quantity_of_seats = models.PositiveSmallIntegerField()
    scheme_of_places = models.TextField(max_length=2000, verbose_name="Схема расположения мест")


class Seat(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, verbose_name="Зал", related_name="cinema_room")
    seat_number = models.PositiveSmallIntegerField()
    is_reserved = models.BooleanField(default=False)


class MovieFormat(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="Тип фильма")
    price_for_adult = models.PositiveIntegerField(default=0)
    price_for_child = models.PositiveIntegerField(default=0)


class ShowTime(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм",)
    showtime = models.DateTimeField(auto_now=False, auto_now_add=False)
    movie_format = models.ForeignKey("MovieFormat", on_delete=models.CASCADE, verbose_name="Формат фильма")
    price_for_adult = models.PositiveIntegerField(default=0)
    price_for_child = models.PositiveIntegerField(default=0)

class RoomFormat(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="Формат зала")
    price_for_adult = models.PositiveIntegerField(default=0)
    price_for_child = models.PositiveIntegerField(default=0)
