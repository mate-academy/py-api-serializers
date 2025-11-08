from rest_framework import serializers

from cinema.models import (
    Movie,
    MovieSession,
    CinemaHall,
    Actor,
    Genre,
    Ticket,
    Order
)


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(
        read_only=True
    )

    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.ListField(
        source="get_genre_names",
        read_only=True
    )
    actors = serializers.ListField(
        source="get_actors_full_names",
        read_only=True
    )


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title"
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name"
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
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


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
