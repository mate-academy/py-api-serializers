from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", )


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", )


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors", )


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall", )


