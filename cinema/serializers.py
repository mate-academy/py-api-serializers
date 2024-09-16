from rest_framework import serializers

from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket)


class CinemaHallSerializers(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return str(obj)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name",)


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id", "title", "description",
            "duration", "genres", "actors"
        )


class MovieListSerializers(MovieSerializers):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)


class MovieDetailSerializers(MovieSerializers):
    genres = GenreSerializers(many=True, read_only=True)
    actors = ActorSerializers(many=True, read_only=True)


class MovieSessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id", "show_time", "movie", "cinema_hall"
        )


class MovieSessionDetailSerializers(MovieSessionSerializers):
    movie = MovieListSerializers(many=False, read_only=True)
    cinema_hall = CinemaHallSerializers(many=False, read_only=True)


class MovieSessionListSerializers(MovieSessionSerializers):
    movie_title = serializers.StringRelatedField(source="movie.title")
    cinema_hall_name = serializers.StringRelatedField(
        source="cinema_hall.name"
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id", "show_time", "movie_title",
            "cinema_hall_name", "cinema_hall_capacity"
        )


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
