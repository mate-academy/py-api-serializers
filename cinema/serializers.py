from rest_framework.fields import (
    CharField,
    IntegerField,
    SerializerMethodField
)
from rest_framework.relations import (
    SlugRelatedField,
    StringRelatedField
)
from rest_framework.serializers import ModelSerializer

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name"
        )


class ActorSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )

    def get_full_name(self, obj) -> str:
        return str(obj)


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"
        )


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
    genres = SlugRelatedField(
        many=True,
        slug_field="name",
        read_only=True
    )
    actors = StringRelatedField(
        many=True,
        read_only=True
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionListSerializer(ModelSerializer):
    movie_title = CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_name = CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
