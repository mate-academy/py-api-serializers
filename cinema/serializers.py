from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cinema.models import (
  Genre,
  Actor,
  CinemaHall,
  Movie,
  MovieSession
)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):


    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(MovieSerializer):
    genres = SlugRelatedField(many=True, read_only=True, slug_field="name")
    actors = SlugRelatedField(many=True, read_only=True, slug_field="full_name")

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"
