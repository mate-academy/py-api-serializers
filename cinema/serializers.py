from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cinema.models import Genre, Actor, Movie, MovieSession


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True
    )
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieSessionSerializer(MovieSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"
