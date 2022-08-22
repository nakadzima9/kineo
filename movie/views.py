import datetime

from rest_framework import viewsets
from users.permissions import IsAdminUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Director, Actor, Genre, Movie
from .serializers import (
    DirectorSerializer,
    ActorSerializer,
    GenreSerializer,
    MovieSerializer,
)


class DirectorModelViewSet(viewsets.ModelViewSet):
    serializer_class = DirectorSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Director.objects.all()


class ActorModelViewSet(viewsets.ModelViewSet):
    serializer_class = ActorSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Actor.objects.all()


class GenreModelViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Genre.objects.all()


class MovieModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Movie.objects.filter(movie_endProduction__gt=datetime.datetime.now())
