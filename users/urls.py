from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import LoginView, ClubCardViewSet, RegisterView

router = DefaultRouter()
router.register(r"club-card", ClubCardViewSet, basename="club-card")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", RegisterView.as_view(), name="register"),
]
