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
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"
        )

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name",)


class ActorSerializer(serializers.ModelSerializer):

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
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        )


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.SerializerMethodField()

    def get_cinema_hall_capacity(self, obj):
        cinema_hall = obj.cinema_hall
        return cinema_hall.seats_in_row * cinema_hall.rows

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(
        many=False,
        read_only=True
    )
    cinema_hall = CinemaHallSerializer(
        many=False,
        read_only=True
    )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            "id",
            "movie_session",
            "order",
            "row",
            "seat"
        )
