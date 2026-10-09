from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return str(obj)


class MovieBaseSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieBaseSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)


class MovieDetailSerializer(MovieBaseSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSessionBaseSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        ]


class MovieSessionDetailSerializer(MovieSessionBaseSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
