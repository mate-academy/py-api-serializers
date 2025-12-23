from typing import Any
from django.db.models import QuerySet
from rest_framework import serializers
from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession
)


class CinemaHallSerializer(serializers.ModelSerializer[CinemaHall]):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer[Genre]):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer[Actor]):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"


class MovieSerializer(serializers.ModelSerializer[Movie]):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")
        read_only_fields = ("id", )


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer[MovieSession]):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
        read_only_fields = ("id",)


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
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
        read_only_fields = ("id",)


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
