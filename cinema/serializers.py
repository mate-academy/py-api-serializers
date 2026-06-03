from typing import Any, Dict
from rest_framework import serializers

from cinema.models import Genre, Movie, Actor, MovieSession, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source="get_full_name", read_only=True
    )

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)
    title = serializers.CharField(required=True)
    duration = serializers.IntegerField(required=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if not attrs.get("title"):
            raise serializers.ValidationError(
                {"title": "This field is required."}
            )
        return attrs


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")

    def validate_title(self, value: str) -> str:
        if not value or len(value.strip()) == 0:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_duration(self, value: int) -> int:
        if value <= 0:
            raise serializers.ValidationError("Duration must be positive.")
        return value


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
        many=True
    )
    actors = serializers.SlugRelatedField(
        slug_field="get_full_name",
        read_only=True,
        many=True
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


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
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


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
