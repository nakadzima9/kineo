from rest_framework import serializers
from .models import Cinema, MovieFormat, Room, RoomFormat, Seat, ShowTime

class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ['cinema_title', 'cinema_description', 'cinema_startTime', 'cinema_endTime', 'cinema_address', 'cinema_website']


class RoomSerializer(serializers.ModelSerializer):
    cinema = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Room
        fields = ['cinema', 'room_name', 'quanity_of_seats', 'scheme_of_places']

class SeatSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = Seat
        fields = ['room', 'seat_number']

class MovieFormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieFormat
        fields = ['type_name', 'price_for_adult', 'price_for_child']

class ShowTime(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField()
    movie = serializers.PrimaryKeyRelatedField()
    movie_format = serializers.PrimaryKeyRelatedField()
    room_format = serializers.PrimaryKeyRelatedField()

    class Meta:
        model = ShowTime
        fields = ['room', 'movie', 'showtime', 'movie_format', 'room_format', 'price_for_adult', 'price_for_child']

class RoomFormat(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['type_name', 'price_for_adult', 'price_for_child']

