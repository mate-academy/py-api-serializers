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
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source="__str__",
        read_only=True
    )

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
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


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

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


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name",
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


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all()
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(
    serializers.ModelSerializer
):
    movie_title = serializers.SlugRelatedField(
        source="movie",
        read_only=True,
        slug_field="title",
    )

    cinema_hall_name = serializers.SlugRelatedField(
        source="cinema_hall",
        read_only=True,
        slug_field="name",
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


class MovieSessionDetailSerializer(
    serializers.ModelSerializer
):
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


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source="user.username"
    )

    class Meta:
        model = Order
        fields = ("id", "created_at")
        read_only_fields = ("user")


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
