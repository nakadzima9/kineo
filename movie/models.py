from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name='Название фильма')
    movie_description = models.TextField(verbose_name='Описание фильма')
    movie_startProduction = models.DateTimeField(auto_now_add=True)
    movie_genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')


class Genre(models.Model):
    genre_title = models.CharField(max_length=42)
    genre_description = models.TextField()
