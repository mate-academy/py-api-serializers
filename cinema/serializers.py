from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "id")
        read_only_fields = ("id",)


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Actor
        fields = ("first_name", "last_name", "full_name", "id")
        read_only_fields = ("id",)


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity", "id")
        read_only_fields = ("id",)


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "id",
            "genres",
            "actors",
        )
        read_only_fields = ("id",)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        genres = GenreSerializer(instance.genres.all(), many=True)
        actors = ActorSerializer(instance.actors.all(), many=True)
        data["genres"] = genres.data
        data["actors"] = actors.data
        return data


class MovieListSerializer(serializers.ModelSerializer):
    genres = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    actors = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
            "id",
        )


class MovieSessionListSerializer(serializers.ModelSerializer):
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )
    cinema_hall_name = serializers.ReadOnlyField(source="cinema_hall.name")

    movie_title = serializers.ReadOnlyField(source="movie.title")

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["movie"] = MovieListSerializer(instance.movie).data
        data["cinema_hall"] = CinemaHallSerializer(instance.cinema_hall).data
        return data
