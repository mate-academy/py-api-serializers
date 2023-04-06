from rest_framework import serializers
from .models import Genre, Movie, Actor, MovieSession, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHall(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=False)  # to return data from relate
    actors = ActorSerializer(many=True, read_only=False)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(
        many=True,
        read_only=True
    )  # to return data from relate
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True
    )


class MovieSessionSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = MovieSession
        fields = "__all__"
