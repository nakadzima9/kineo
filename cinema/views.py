from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminUserOrReadOnly
from .models import Cinema, MovieFormat, Room, RoomFormat, Seat, ShowTime
from .serializers import (
    CinemaSerializer,
    MovieFormatSerializer,
    RoomSerializer,
    RoomFormatSerializer,
    SeatSerializer,
    ShowTimeSerializer,
)


class CinemaModelViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Cinema.objects.all()


class MovieFormatModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = MovieFormat.objects.all()


class RoomModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Room.objects.all()


class RoomFormatModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoomFormatSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = RoomFormat.objects.all()


class SeatModelViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = Seat.objects.all()


class ShowTimeModelViewSet(viewsets.ModelViewSet):
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = ShowTime.objects.all()
