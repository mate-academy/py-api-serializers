
from rest_framework.fields import SerializerMethodField, ReadOnlyField
from rest_framework.relations import PrimaryKeyRelatedField, SlugRelatedField
from rest_framework.serializers import ModelSerializer

from cinema.models import (
    CinemaHall,
    Genre,
    Actor, Movie, MovieSession, Order, Ticket)


class CinemaHallSerializer(ModelSerializer):
    capacity = ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name", )


class ActorSerializer(ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)


class MovieListSerializer(MovieSerializer):
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


class MovieSessionSerializer(ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "movie", "show_time", "cinema_hall")


class MovieSessionDetailsSerializer(ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
    movie_id = PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source="movie",
        write_only=True
    )
    cinema_hall_id = PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        source="cinema_hall",
        write_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "movie",
            "show_time",
            "cinema_hall",
            "movie_id",
            "cinema_hall_id"
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = SlugRelatedField(
        source="movie",
        read_only=True,
        slug_field="title",
    )
    cinema_hall_name = SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="name"
    )
    cinema_hall_capacity = SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="capacity",
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "movie",
            "cinema_hall_capacity",
            "movie_title",
            "cinema_hall_name"
        )


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("created_at", "user")


# class OrderListSerializer(OrderSerializer):
    # user = UserSerialize()


class TicketSerializer(ModelSerializer):
    movie_session = MovieSessionListSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("movie_session", "order", "row", "seat")


class TicketListSerializer(TicketSerializer):
    movie_session = MovieSessionSerializer()
    order = OrderSerializer()
