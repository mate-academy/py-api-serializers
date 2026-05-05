from django.db.models import QuerySet
from rest_framework import serializers

from cinema.models import (
    Movie,
    MovieSession,
    CinemaHall,
    Genre,
    Actor,
    Order,
    Ticket
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


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
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

    def get_queryset(self) -> QuerySet[CinemaHall]:
        return self.queryset


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name"
        )

    def get_queryset(self) -> QuerySet[Genre]:
        return self.queryset


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )

    def get_queryset(self) -> QuerySet[Actor]:
        return self.queryset


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user"
        )

    def get_queryset(self) -> QuerySet[Order]:
        return self.queryset


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

    def get_queryset(self) -> QuerySet[Ticket]:
        return self.queryset


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True,
    )
    actors = ActorSerializer(
        many=True,
        read_only=True,
    )

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


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
