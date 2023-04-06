from rest_framework import serializers

from . import models


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = (
            "id",
            "name",
        )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )


class MovieListSerializer(MovieSerializer):
    actors = serializers.SlugRelatedField(
        slug_field="full_name", many=True, read_only=True
    )
    genres = serializers.SlugRelatedField(
        slug_field="name", many=True, read_only=True
    )


class MovieDetailSerializer(MovieSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MovieSession
        fields = (
            "id",
            "show_time",
            "cinema_hall",
            "movie",
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", max_length=255)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", max_length=255
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = models.MovieSession
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
            "cinema_hall_capacity",
        ]


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = models.MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )
