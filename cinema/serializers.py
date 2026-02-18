from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    IntegerField,
    SlugRelatedField,
    PrimaryKeyRelatedField,
    StringRelatedField,
)

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ["id"]


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]
        read_only_fields = ["id"]


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = [
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        ]
        read_only_fields = ["id"]


class MovieSerializer(ModelSerializer):
    genres = PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
    )
    actors = PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        ]
        read_only_fields = ["id"]


class MovieListSerializer(MovieSerializer):
    genres = StringRelatedField(
        many=True,
    )
    actors = StringRelatedField(
        many=True,
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ["id"]


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = CharField(source="movie.title", read_only=True)
    cinema_hall_name = CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = IntegerField(
        source="cinema_hall.capacity",
        read_only=True,
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
