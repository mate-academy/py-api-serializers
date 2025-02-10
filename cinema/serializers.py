from rest_framework import serializers
from rest_framework.fields import SlugField

from cinema import models


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.StringRelatedField(many=True)


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = models.MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        ]


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()
