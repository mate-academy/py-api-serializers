from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import (
    SerializerMethodField,
    IntegerField,
    CharField
)
from rest_framework.serializers import ModelSerializer

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    @staticmethod
    def get_full_name(obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieSerializer):
    genres = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = StringRelatedField(
        many=True,
        read_only=True,
    )


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(Genre, many=True)
    actors = ActorSerializer(Actor, many=True)


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(ModelSerializer):
    movie_title = CharField(source="movie.title", read_only=True)
    cinema_hall_name = CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = IntegerField(
        source="cinema_hall.capacity"
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


class MovieSessionDetailSerializer(ModelSerializer):
    movie = MovieListSerializer(Movie, many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(CinemaHall, many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
