from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity",)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall",)


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")
