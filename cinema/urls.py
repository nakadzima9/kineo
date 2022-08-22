from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CinemaModelViewSet,
    MovieFormatModelViewSet,
    RoomModelViewSet,
    RoomFormatModelViewSet,
    SeatModelViewSet,
    ShowTimeModelViewSet,
)

router = DefaultRouter()
router.register(r"movie-format", MovieFormatModelViewSet, basename="movie-format")
router.register(r"showtime", ShowTimeModelViewSet, basename="showtime")
router.register(r"seat", SeatModelViewSet, basename="seat")
router.register(r"room-format", RoomFormatModelViewSet, basename="room-format")
router.register(r"room", RoomModelViewSet, basename="room")
router.register(r"", CinemaModelViewSet, basename="cinema")

urlpatterns = [
    path("", include(router.urls)),
]
