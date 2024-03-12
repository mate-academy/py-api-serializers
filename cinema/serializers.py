from rest_framework import serializers
from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name")
    actors = serializers.StringRelatedField(many=True)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
    show_time = serializers.IntegerField(
        source="movie.duration",
        read_only=True)
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True)

    class Meta(CinemaHallSerializer.Meta):
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    show_time = serializers.IntegerField(
        source="movie.duration",
        read_only=True)
    cinema_hall = CinemaHallSerializer()

    class Meta(CinemaHallSerializer.Meta):
        fields = ["id", "show_time", "movie", "cinema_hall"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionSerializer()
    order = OrderSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"
