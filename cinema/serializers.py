"""Read and write representations for cinema resources."""
from __future__ import annotations

from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    """Serialize and validate a genre."""

    class Meta:
        model = Genre
        fields: tuple[str, ...] = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    """Expose a computed full name alongside writable name fields."""

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, actor: Actor) -> str:
        return f"{actor.first_name} {actor.last_name}"

    class Meta:
        model = Actor
        fields: tuple[str, ...] = (
            "id", "first_name", "last_name", "full_name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    """Expose the model's calculated capacity as read-only."""

    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields: tuple[str, ...] = (
            "id", "name", "rows", "seats_in_row", "capacity",
        )


class MovieSerializer(serializers.ModelSerializer):
    """Accept existing actor and genre IDs for write operations."""

    class Meta:
        model = Movie
        fields: tuple[str, ...] = (
            "id", "title", "description", "duration", "genres", "actors",
        )


class MovieListSerializer(MovieSerializer):
    """Return genre names and actor full names in movie lists."""

    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.StringRelatedField(many=True)


class MovieDetailSerializer(MovieSerializer):
    """Include complete actor and genre objects when retrieving a movie."""

    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    """Accept movie and hall IDs when creating or updating a session."""

    class Meta:
        model = MovieSession
        fields: tuple[str, ...] = (
            "id", "show_time", "movie", "cinema_hall",
        )


class MovieSessionListSerializer(serializers.ModelSerializer):
    """Flatten related information for the session list."""

    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields: tuple[str, ...] = (
            "id", "show_time", "movie_title",
            "cinema_hall_name", "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    """Nest the movie summary and complete hall representation."""

    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
