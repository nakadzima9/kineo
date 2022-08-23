from rest_framework import serializers
from .models import Ticket, TicketType, PurchaseHistory, Booking, PayMethod, Order
from cinema.models import Seat, ShowTime
from users.models import User


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ["id", "name"]


class TicketSerializer(serializers.ModelSerializer):
    ticket_type = serializers.PrimaryKeyRelatedField(queryset=TicketType.objects.all())
    showtime = serializers.PrimaryKeyRelatedField(queryset=ShowTime.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    class Meta:
        model = Ticket
        fields = ["id", "ticket_type", "showtime", "seat", "price"]
        read_only_fields = ["price"]


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())

    class Meta:
        model = Booking
        fields = ["id", "user", "ticket", "when_reserved"]

    def validate(self, attrs):
        ticket = attrs.get("ticket")
        seat = ticket.seat
        showtime = ticket.showtime
        query = Booking.objects.filter(ticket__seat=seat, ticket__showtime=showtime)
        if query.exists():
            raise serializers.ValidationError("This seat is already reserved")
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    purchase_history = serializers.PrimaryKeyRelatedField(
        queryset=PurchaseHistory.objects.all()
    )
    ticket = serializers.PrimaryKeyRelatedField(queryset=Ticket.objects.all())
    pay_method = serializers.PrimaryKeyRelatedField(queryset=PayMethod.objects.all())

    class Meta:
        model = Order
        fields = ["id", "purchase_history", "ticket", "pay_method"]


class PurchaseHistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    total_costs = serializers.SerializerMethodField(method_name="get_total_costs")

    class Meta:
        model = PurchaseHistory
        fields = ["id", "user", "total_costs"]
        read_only_fields = ["total_costs"]

    def get_total_costs(self, obj):
        buff = Order.objects.filter(purchase_history=obj.pk)
        if buff.exists():
            total_costs = sum([order.ticket.price for order in buff])
            return total_costs
        return 0


class PayMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayMethod
        fields = ["id", "name"]
