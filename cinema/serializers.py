from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)
from .constants import (
    FIELDS_ACTOR,
    FIELDS_COMMON,
    FIELDS_SHOWTIME,
    FIELDS_CINEMA_HALL,
    FIELDS_GENRE,
)
from django.utils.translation import gettext_lazy as _


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = FIELDS_GENRE


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = FIELDS_ACTOR

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = FIELDS_CINEMA_HALL


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = FIELDS_COMMON


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = FIELDS_SHOWTIME


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta(MovieSessionSerializer.Meta):
        fields = MovieSessionSerializer.Meta.fields + (
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta(MovieSessionSerializer.Meta):
        fields = MovieSessionSerializer.Meta.fields + (
            "movie",
            "cinema_hall",
        )
        extra_kwargs = {
            "movie": {"required": True},
            "cinema_hall": {"required": True},
        }
