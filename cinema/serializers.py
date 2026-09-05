from django.contrib.auth import get_user_model
from cinema.models import (CinemaHall, Genre, Actor, Movie, MovieSession,
                           Order, Ticket)
from rest_framework import serializers
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]
        read_only_fields = ["id"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ["id"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class ActorRetrieveSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration",
                  "genres", "actors"]
        read_only_fields = ["id"]


class MovieListSerializer(MovieSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_genres(self, obj) -> list[str]:
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj) -> list[str]:
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorRetrieveSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ["id"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    show_time = serializers.DateTimeField()
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title", "cinema_hall_name",
                  "cinema_hall_capacity"]


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "created_at", "user"]
        read_only_fields = ["id"]


class OrderListSerializer(OrderSerializer):
    user = UserSerializer()


class OrderRetrieveSerializer(OrderSerializer):
    user = UserSerializer()


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "movie_session", "order", "row", "seat"]
        read_only_fields = ["id"]


class TicketListSerializer(TicketSerializer):
    movie_session = MovieSessionSerializer()
    order = OrderSerializer()


class TicketRetrieveSerializer(TicketSerializer):
    movie_session = MovieSessionListSerializer()
    order = OrderSerializer()
