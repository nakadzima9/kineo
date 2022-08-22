from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsAdminUserOrReadOnly, IsOwnerOrAdmin
from .models import Booking, PayMethod, PurchaseHistory, Ticket, TicketType, Order
from .serializers import (
    BookingSerializer,
    PayMethodSerializer,
    PurchaseHistorySerializer,
    TicketSerializer,
    TicketTypeSerializer,
    OrderSerializer,
)


class OrderModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]
    queryset = Order.objects.all()


class TicketModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()


class TicketTypeModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class BookingModelViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]
    queryset = Booking.objects.all()


class PurchaseHistoryModelViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseHistorySerializer
    permission_classes = [IsAuthenticated & IsOwnerOrAdmin]
    queryset = PurchaseHistory.objects.all()


class PayMethodModelViewSet(viewsets.ModelViewSet):
    serializer_class = PayMethodSerializer
    permission_classes = [IsAuthenticated & IsAdminUserOrReadOnly]
    queryset = PayMethod.objects.all()
