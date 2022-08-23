from rest_framework import serializers
from .models import Cinema, MovieFormat, Room, RoomFormat, Seat, ShowTime
from movie.models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = [
            "id",
            "cinema_title",
            "cinema_description",
            "cinema_startTime",
            "cinema_endTime",
            "cinema_address",
            "cinema_website",
        ]


class RoomSerializer(serializers.ModelSerializer):
    cinema = serializers.PrimaryKeyRelatedField(queryset=Cinema.objects.all())

    class Meta:
        model = Room
        fields = ["id", "cinema", "room_name", "quantity_of_seats", "scheme_of_places"]


class SeatSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())

    class Meta:
        model = Seat
        fields = ["id", "room", "seat_number"]


class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = ["id", "type_name", "price_for_adult", "price_for_child"]


class RoomFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomFormat
        fields = ["id", "type_name", "price_for_adult", "price_for_child"]


class ShowTimeSerializer(serializers.ModelSerializer):
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    movie_format = serializers.PrimaryKeyRelatedField(
        queryset=MovieFormat.objects.all()
    )
    room_format = serializers.PrimaryKeyRelatedField(queryset=RoomFormat.objects.all())

    class Meta:
        model = ShowTime
        fields = [
            "room",
            "movie",
            "showtime",
            "movie_format",
            "room_format",
            "price_for_adult",
            "price_for_child",
        ]
