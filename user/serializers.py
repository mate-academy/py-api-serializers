from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from user.models import User


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieRetrieveSerializer(MovieSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.ReadOnlyField()
    cinema_hall_name = serializers.ReadOnlyField()
    cinema_hall_capacity = serializers.ReadOnlyField()

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

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )
