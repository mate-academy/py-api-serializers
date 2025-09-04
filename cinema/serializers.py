from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession
from typing import List, Type


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name: serializers.CharField = serializers.CharField(
        source="__str__", read_only=True
    )

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity: serializers.IntegerField = (
        serializers.IntegerField(read_only=True)
    )

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieListSerializer(serializers.ModelSerializer):
    genres: serializers.SlugRelatedField = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors: serializers.SerializerMethodField = (
        serializers.SerializerMethodField()
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

    def get_actors(self, obj: Movie) -> List[str]:
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres: GenreSerializer = GenreSerializer(many=True, read_only=True)
    actors: ActorSerializer = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title: serializers.CharField = (
        serializers.CharField(source="movie.title", read_only=True)
    )
    cinema_hall_name: serializers.CharField = (
        serializers.CharField(source="cinema_hall.name", read_only=True)
    )
    cinema_hall_capacity: serializers.IntegerField = (
        serializers.IntegerField(source="cinema_hall.capacity", read_only=True)
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


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie: MovieListSerializer = MovieListSerializer(read_only=True)
    cinema_hall: CinemaHallSerializer = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
