from django.db import models


class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name='Название фильма')
    movie_description = models.TextField(verbose_name='Описание фильма')
    movie_startProduction = models.DateTimeField(auto_now_add=True)
    movie_genre = models.ForeignKey('Genre', on_delete=models.CASCADE, verbose_name='Жанр')


class Director(models.Model):
    director_name = models.CharField(max_length=255, verbose_name='Режиссёр')
    director_career = models.TextField()
    director_date_of_birth = models.CharField(max_length=100, verbose_name='Дата рождения')
    director_place_of_birth = models.CharField(max_length=100, verbose_name='Место рождения')
    movie_director = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Genre(models.Model):
    genre_title = models.CharField(max_length=42)
    genre_description = models.TextField()
