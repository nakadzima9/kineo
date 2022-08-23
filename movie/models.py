from django.db import models
from datetime import date
from django.utils import timezone


class Director(models.Model):
    director_name = models.CharField(max_length=255, verbose_name="Имя")
    director_career = models.TextField(verbose_name="Описание")
    director_date_of_birth = models.DateField(
        default=date.today, verbose_name="Дата рождения"
    )
    director_place_of_birth = models.CharField(
        max_length=100, verbose_name="Место рождение"
    )

    def __str__(self):
        return self.director_name

    class Meta:
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Actor(models.Model):
    actor_name = models.CharField(max_length=100, verbose_name="Имя")
    actor_career = models.TextField(verbose_name="Описание")
    actor_date_of_birth = models.DateField(
        default=date.today, verbose_name="Дата рождения"
    )
    actor_place_of_birth = models.CharField(
        max_length=100, verbose_name="Место рождение"
    )

    def __str__(self):
        return self.actor_name

    class Meta:
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"


class Genre(models.Model):
    genre_title = models.CharField(max_length=50, verbose_name="Название")
    genre_description = models.TextField(verbose_name="Описание жанра")

    def __str__(self):
        return self.genre_title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    movie_title = models.CharField(max_length=100, verbose_name="Название фильма")
    movie_description = models.TextField(verbose_name="Описание фильма")
    movie_poster = models.ImageField(upload_to="movies/", verbose_name="Постер")
    movie_year = models.PositiveSmallIntegerField(
        default=2022, verbose_name="Дата выхода"
    )
    movie_country = models.CharField(max_length=50, verbose_name="Страна")
    movie_director = models.ManyToManyField(
        Director, verbose_name="Режиссёр", related_name="film_director"
    )
    movie_actor = models.ManyToManyField(
        Actor, verbose_name="Актёр", related_name="film_actor"
    )
    movie_genre = models.ManyToManyField(
        Genre, verbose_name="Жанр", related_name="film_genre"
    )
    movie_duration = models.CharField(max_length=50, verbose_name="Длительность")
    movie_trailer = models.URLField(
        max_length=200, null=True, blank=True, verbose_name="Трейлер фильма"
    )
    movie_startProduction = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="Фильм в прокате"
    )
    movie_endProduction = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name="Фильм снят с проката"
    )
    is_production = models.BooleanField(blank=True, null=True, verbose_name="В прокате")
    age_rating = models.PositiveSmallIntegerField(
        default=0, verbose_name="Возрастной рейтинг"
    )

    def save(self, *args, **kwargs):
        self.is_production = False
        if (
            self.movie_startProduction
            <= timezone.now().date()
            <= self.movie_endProduction
        ):
            self.is_production = True
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.movie_title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
