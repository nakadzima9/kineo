from django.db import models


class Cinema(models.Model):
    cinema_title = models.CharField(max_length=255, verbose_name='Название кинотеатра')
    cinema_description = models.TextField(verbose_name='Описание кинотеатра')
    cinema_startTime = models.DateTimeField(auto_now_add=True)
    cinema_endTime = models.DateTimeField(auto_now_add=True)
    cinema_address = models.CharField(max_length=255, verbose_name='Адрес кинотеатра')
    cinema_website = models.URLField(max_length=200, null=True, blank=True)


class Room(models.Model):
    pass


class ShowTime(models.Model):
    pass
