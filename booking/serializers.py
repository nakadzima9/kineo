from rest_framework import serializers
from .models import Ticket, TicketType, PurchaseHistory, Booking, PayMethod, Order


class TicketSerializer(serializers.ModelSerializer):
    ticket_type = serializers.PrimaryKeyRelatedField()
    showtime = serializers.PrimaryKeyRelatedField()
    seat = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Ticket
        fields = ['ticket_type', 'showtime', 'seat', 'price', ]


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ['__all__']


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField()
    ticket = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Booking
        fields = ['user', 'ticket', 'when_reserved']

    def validate(self, attrs):
        ticket = attrs.get('ticket')
        seat = ticket.seat
        showtime = ticket.showtime
        query = Booking.objects.filter(ticket_seat=seat, ticket_showtime=showtime)
        if query.exists():
            raise serializers.ValidationError('This seat is already reserved')
        return attrs


class OrderSerializer(serializers.ModelSerializer):
    purchase_history = serializers.PrimaryKeyRelatedField()
    ticket = serializers.PrimaryKeyRelatedField()
    pay_method = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Order
        fields = ['purchase_history', 'ticket', 'pay_method']


class PurchaseHistory(serializers.PrimaryKeyRelatedField):
    owner = serializers.PrimaryKeyRelatedField()
    total_costs = serializers.SerializerMethodField(method_name='get_total_costs')

    class Meta:
        model = PurchaseHistory
        fields = ['owner', 'total_costs']
        read_only_fields = ['total_costs']

    def get_total_costs(self, obj):
        buff = Order.objects.filter(purchase_history=obj.pk)
        if buff.exists():
            total_costs = sum([order.ticket.price for order in buff])
            return total_costs
        return 0


class PayMethod(serializers.ModelSerializer):
    class Meta:
        model = PayMethod
        fields = ['__all__']
