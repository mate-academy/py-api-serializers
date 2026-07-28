from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework.fields import CharField, IntegerField
from rest_framework.relations import PrimaryKeyRelatedField

from cinema.models import (
    Actor,
    CinemaHall,
    Genre,
    Movie,
    MovieSession,
    Order,
    Ticket
)


class ActorSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieListSerializer(ModelSerializer):
    genres = SerializerMethodField()
    actors = SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieDetailSerializer(ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieCreateSerializer(ModelSerializer):
    genres = PrimaryKeyRelatedField(queryset=Genre.objects.all(), many=True)
    actors = PrimaryKeyRelatedField(queryset=Actor.objects.all(), many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionDetailSerializer(ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(ModelSerializer):
    movie_title = CharField(source="movie.title")
    cinema_hall_name = CharField(source="cinema_hall.name")
    cinema_hall_capacity = IntegerField(source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionCreateSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "created_at", "user")


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "movie_session", "order", "row", "seat")
