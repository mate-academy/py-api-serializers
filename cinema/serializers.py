from rest_framework import serializers

from cinema.models import (
    Genre,
    Movie,
    Actor,
    CinemaHall,
    MovieSession
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True
    )
    actors = ActorSerializer(
        many=True,
        read_only=True
    )


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
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


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieRetrieveSerializer(
        read_only=True,
    )
    cinema_hall = CinemaHallSerializer(
        read_only=True,
    )
