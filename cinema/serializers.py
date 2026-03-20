from typing import Any

from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer

from cinema.models import (CinemaHall, Genre, Ticket, Order, MovieSession, Movie, Actor)


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name",)


class ActorDetailSerializer(ActorSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class MovieListSerializer(ModelSerializer):
    genres = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    actors = StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors",)


class MovieDetailSerializer(MovieListSerializer):
    actors = ActorDetailSerializer(many=True)
    genres = GenreSerializer(many=True)


class MovieDetailPostSerializer(MovieDetailSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    def create(self, validated_data) -> Movie:
        genres = validated_data.pop("genres", None)
        actors = validated_data.pop("actors", None)

        movie = Movie.objects.create(**validated_data)

        if genres is not None:
            movie.genres.set(genres)
        if actors is not None:
            movie.actors.set(actors)

        return movie

    def update(self, instance, validated_data) -> Any:
        genres = validated_data.pop("genres", None)
        actors = validated_data.pop("actors", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)

        return instance


class MovieSessionSerializer(ModelSerializer):
    movie_title = SlugRelatedField(
        source="movie",
        read_only=True,
        slug_field="title"
    )

    cinema_hall_name = SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="name"
    )

    cinema_hall_capacity = SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="capacity"
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerializer(ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionPostSerializer(ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all()
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ("show_time", "movie", "cinema_hall")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("movie_session", "order", "row", "seat",)
