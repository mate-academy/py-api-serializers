from typing import Any

from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def to_representation(self, instance: Movie) -> dict[str, Any]:
        data = super().to_representation(instance)

        data["genres"] = [g.name for g in instance.genres.all()]
        data["actors"] = [
            f"{a.first_name} {a.last_name}"
            for a in instance.actors.all()
        ]

        return data


class MovieListSerializer(MovieSerializer):
    pass


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "movie", "cinema_hall", "show_time"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
            "show_time",
        ]


class MovieSessionMovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_genres(self, obj: Movie) -> list[str]:
        return [g.name for g in obj.genres.all()]

    def get_actors(self, obj: Movie) -> list[str]:
        return [f"{a.first_name} {a.last_name}" for a in obj.actors.all()]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieSessionMovieSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ["id", "movie", "cinema_hall", "show_time"]
