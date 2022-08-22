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

    class Meta:
        verbose_name = "Кинотеатр"
        verbose_name_plural = "Кинотеатры"


class Room(models.Model):
    cinema = models.ForeignKey('Cinema', on_delete=models.CASCADE, verbose_name="Кинотеатр")
    room_name = models.CharField(max_length=50, verbose_name="Зал")
    quantity_of_seats = models.PositiveSmallIntegerField(verbose_name="Количество мест")
    scheme_of_places = models.TextField(max_length=2000, verbose_name="Схема расположения мест")

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = "Зал"
        verbose_name_plural = "Залы"


class Seat(models.Model):
    room = models.ForeignKey("Room", on_delete=models.CASCADE, verbose_name="Зал", related_name="cinema_room")
    seat_number = models.PositiveSmallIntegerField(verbose_name="Номер места")

    def __str__(self):
        return f"Seat:{self.seat_number}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class MovieFormat(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="Тип фильма")
    price_for_adult = models.PositiveIntegerField(default=0, verbose_name="Цена взрослый")
    price_for_child = models.PositiveIntegerField(default=0, verbose_name="Цена детский")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = "Формат фильма"


class ShowTime(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, verbose_name="Зал")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фильм")
    showtime = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name="Время показа")
    movie_format = models.ForeignKey("MovieFormat", on_delete=models.CASCADE, verbose_name="Формат фильма")
    room_format = models.ForeignKey('RoomFormat', on_delete=models.CASCADE, verbose_name='Формат зала')
    price_for_adult = models.PositiveIntegerField(default=0, verbose_name="Цена взрослый")
    price_for_child = models.PositiveIntegerField(default=0, verbose_name="Цена детский")

    def __str__(self):
        return self.showtime.strftime("%Y/%m/%d, %H:%M:%S")

    class Meta:
        verbose_name_plural = "Время показа"


class RoomFormat(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="Формат зала")
    price_for_adult = models.PositiveIntegerField(default=0, verbose_name="Цена взрослый")
    price_for_child = models.PositiveIntegerField(default=0, verbose_name="Цена детский")

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name_plural = "Формат зала"
