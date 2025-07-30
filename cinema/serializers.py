from django.db.models import Count
from rest_framework import serializers
from django.db.models import F, Value
from django.db.models.functions import Concat

from .models import (
    CinemaHall, Genre, Actor,
    Movie, MovieSession, Order,
    Ticket,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj): # noqa -> unreal to do it static
        return obj.genres.values_list("name", flat=True)

    def get_actors(self, obj): # noqa -> unreal to do it static
        return obj.actors.annotate(
            full_name=Concat(F("first_name"), Value(" "), F("last_name"))
        ).values_list("full_name", flat=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity")


class OrderSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):

    movie_session = MovieSessionSerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id", "movie_session", "order",
            "row", "seat"
        )
