from rest_framework import serializers

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)


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


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name",)


class GenreDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("first_name", "last_name", "full_name", )


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

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


class MovieDetailSerializer(MovieSerializer):
    genres = GenreDetailSerializer(many=True)
    actors = ActorDetailSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title")
    cinema_hall_name = serializers.ReadOnlyField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
