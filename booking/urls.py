from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    OrderModelViewSet,
    TicketModelViewSet,
    TicketTypeModelViewSet,
    BookingModelViewSet,
    PurchaseHistoryModelViewSet,
    PayMethodModelViewSet,
)

router = DefaultRouter()
router.register(r"booking", BookingModelViewSet, basename="booking")
router.register(r"pay-method", PayMethodModelViewSet, basename="pay-method")
router.register(
    r"purchase-history", PurchaseHistoryModelViewSet, basename="purchase-histroy"
)
router.register(r"ticket", TicketModelViewSet, basename="ticket")
router.register(r"ticket-type", TicketTypeModelViewSet, basename="ticket-type")
router.register(r"", OrderModelViewSet, basename="order")

urlpatterns = [
    path("", include(router.urls)),
]
