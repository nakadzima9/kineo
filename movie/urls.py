from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    DirectorModelViewSet,
    ActorModelViewSet,
    GenreModelViewSet,
    MovieModelViewSet,
)

router = DefaultRouter()
router.register(r"actor", ActorModelViewSet, basename="actor")
router.register(r"director", DirectorModelViewSet, basename="director")
router.register(r"genre", GenreModelViewSet, basename="genre")
router.register(r"film", MovieModelViewSet, basename="film")

urlpatterns = [
    path("", include(router.urls)),
]
