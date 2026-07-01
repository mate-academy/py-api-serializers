from rest_framework import serializers
from .models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket
)
# write serializers here
from rest_framework import serializers
from cinema.models import (
    Actor,
    Movie,
    MovieSession,
    CinemaHall,
    Genre,
    Ticket,
    Order
)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["genres"] = GenreSerializer(
            instance.genres.all(), many=True).data
        representation["actors"] = ActorSerializer(
            instance.actors.all(), many=True).data
        return representation


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.SlugRelatedField(
        slug_field="title",
        queryset=Movie.objects.all(),
        source="movie"
    )
    cinema_hall_name = serializers.StringRelatedField(
        source="cinema_hall"
    )
    cinema_hall_capacity = serializers.SlugRelatedField(
        slug_field="capacity",
        queryset=CinemaHall.objects.all(),
        source="cinema_hall"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all())

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["movie"] = MovieSerializer(instance.movie).data
        representation["cinema_hall"] = CinemaHallSerializer(
            instance.cinema_hall).data
        return representation


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
