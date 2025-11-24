from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from typing import Any, Dict, List

from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj: Movie) -> List[str]:
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj: Movie) -> List[str]:
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
    genres_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        write_only=True,
        many=True,
        required=True
    )
    actors_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        write_only=True,
        many=True,
        required=True
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration",
                  "genres", "actors", "genres_ids", "actors_ids")

    def validate_genres_ids(self, value: List[Genre]) -> List[Genre]:
        if not value:
            raise serializers.ValidationError(
                "At least one genre must be provided."
            )
        return value

    def validate_actors_ids(self, value: List[Actor]) -> List[Actor]:
        if not value:
            raise serializers.ValidationError(
                "At least one actor must be provided."
            )
        return value

    def create(self, validated_data: Dict[str, Any]) -> Movie:
        genres = validated_data.pop("genres_ids", [])
        actors = validated_data.pop("actors_ids", [])
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        movie.actors.set(actors)
        return movie

    def update(self, instance: Movie, validated_data: Dict[str, Any]) -> Movie:
        genres = validated_data.pop("genres_ids", None)
        actors = validated_data.pop("actors_ids", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)

        return instance


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name",
                                             read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta(MovieSessionSerializer.Meta):
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    cinema_hall_id = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        write_only=True,
        required=True,
        source="cinema_hall"
    )

    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        write_only=True,
        required=True,
        source="movie"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
            "cinema_hall_id",
            "movie_id"
        )

    def create(self, validated_data: Dict[str, Any]) -> MovieSession:
        return super().create(validated_data)

    def update(
            self,
            instance: MovieSession,
            validated_data: Dict[str, Any]
    ) -> MovieSession:
        return super().update(instance, validated_data)
