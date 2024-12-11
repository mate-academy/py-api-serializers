from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieSerializer):
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class MovieDetailSerializer(MovieSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        exclude = ["movie", "cinema_hall"]


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "created_at", "user"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "movie_session", "order", "row", "seat"]
