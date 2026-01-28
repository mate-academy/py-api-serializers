from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from typing import Dict

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


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


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"
        )


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
    )

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

    def create(self, validated_data: Dict) -> Movie:
        genres_data = validated_data.pop("genres", None)
        actors_data = validated_data.pop("actors", None)
        movie = Movie.objects.create(**validated_data)
        if genres_data:
            movie.genres.set(genres_data)
        if actors_data:
            movie.actors.set(actors_data)
        return movie

    def update(self, instance: Movie, validated_data: Dict) -> Movie:
        genres_data = validated_data.pop("genres", None)
        actors_data = validated_data.pop("actors", None)
        if genres_data:
            instance.genres.set(genres_data)
        if actors_data:
            instance.actors.set(actors_data)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)
    # figure out how to display actors 'full_name' fields instead of pk

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


class MovieRetrieveSerializer(MovieListSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

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


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie = PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        write_only=True
    )
    cinema_hall = PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        write_only=True
    )
    movie_title = serializers.StringRelatedField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.StringRelatedField(
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
            "cinema_hall_capacity",
            "movie",
            "cinema_hall"
        )


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = PrimaryKeyRelatedField(queryset=CinemaHall.objects.all())

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
