from rest_framework import serializers
from .models import Actor, Genre, Movie, MovieSession, CinemaHall
from typing import List


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name",)


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, obj: Movie) -> List[str]:
        return [f"{a.first_name} {a.last_name}" for a in obj.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
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
            "actors",
        )


class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        allow_empty=False
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        allow_empty=False
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def validate_duration(self, value: int) -> int:
        if value <= 0:
            raise serializers.ValidationError("Duration must be positive.")
        return value

    def validate_title(self, value: str) -> str:
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
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


class MovieNestedSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField()

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

    def get_actors(self, obj: Movie) -> List[str]:
        return [f"{a.first_name} {a.last_name}" for a in obj.actors.all()]


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all()
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieNestedSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
