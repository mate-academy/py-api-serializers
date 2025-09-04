from rest_framework import serializers

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
    Order,
    Ticket
)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name", )


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)


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


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "movie", "show_time", "cinema_hall")


class MovieSessionDetailsSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source="movie",
        write_only=True
    )
    cinema_hall_id = serializers.PrimaryKeyRelatedField(
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
    movie_title = serializers.SlugRelatedField(
        source="movie",
        read_only=True,
        slug_field="title",
    )
    cinema_hall_name = serializers.SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="name"
    )
    cinema_hall_capacity = serializers.SlugRelatedField(
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


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ("created_at", "user")


class TicketSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionListSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = ("movie_session", "order", "row", "seat")
