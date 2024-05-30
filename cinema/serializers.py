from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    CharField,
    IntegerField,
)

from cinema.models import Genre, Actor, CinemaHall, MovieSession, Movie


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )


class CinemaHallSerializer(ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
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
            "actors",
        )


class MovieListSerializer(MovieSerializer):
    genres = SlugRelatedField(many=True, read_only=True, slug_field="name")
    actors = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(MovieSerializer):

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False)
    cinema_hall = CinemaHallSerializer(many=False)


class MovieSessionListSerializer(ModelSerializer):
    movie_title = CharField(source="movie.title", read_only=True)
    cinema_hall_name = CharField(source="cinema_hall.name", read_only=True)
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
