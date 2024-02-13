from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        )


class MovieListSerializer(MovieSerializer):
    genres = StringRelatedField(many=True, read_only=True)
    actors = StringRelatedField(many=True, read_only=True)


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False)
    cinema_hall = CinemaHallSerializer(many=False)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall",)
