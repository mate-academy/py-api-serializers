from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    MovieSession,
    Movie
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres"
        ]


class MovieListSerializer(MovieSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)


class MovieDetailSerializer(MovieSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)
    movie = MovieDetailSerializer(many=False, read_only=True)


class MovieSessionListSerializer(
    MovieSessionSerializer
):
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )
