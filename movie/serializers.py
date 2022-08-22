from rest_framework import serializers
from .models import Movie, Genre, Actor, Director


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['genre_title', 'genre_description']


class ActorSerializer(serializers.ModelSerializer):
    actor_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Actor
        fields = ['actor_name', 'actor_career', 'actor_date_of_birth', 'actor_place_of_birth', 'actor_image']


class DirectorSerializer(serializers.ModelSerializer):
    director_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Director
        fields = ['director_name', 'directorn_career', 'director_date_of_birth', 'director_place_of_birth', 'director_image']


class MovieSerializer(serializers.ModelSerializer):
    movie_poster = serializers.ImageField(max_length=None ,use_url=True)
    movie_director = DirectorSerializer(many=True)
    movie_actor = ActorSerializer(many=True)
    movie_genre = GenreSerializer(many= True)

    class Meta:
        model = Movie
        fields = ['movie_title', 'movie_description', 'movie_poster', 'movie_year', 'movie_country', 'movie_director', 'movie_actor', 'movie_genre', 'movie_duration', 'movie_trailer', 'movie_trailer', 'movie_startProduction', 'movie_endProduction', 'is_production', 'age_rating']

