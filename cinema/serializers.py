from rest_framework import serializers
from .models import Genre, Movie, Actor, MovieSession, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
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


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(
        many=True, read_only=True
    )
    actors = serializers.StringRelatedField(
        many=True, read_only=True
    )


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "cinema_hall",
            "movie",
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(
        source="movie.title", max_length=255
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", max_length=255
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta(MovieSessionSerializer.Meta):
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )
        read_only_fields = [
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        ]


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()
