from rest_framework import serializers
from cinema.models import Movie, Actor, Genre, MovieSession, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return str(obj)


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)
    actors = serializers.SlugRelatedField(slug_field="full_name", many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "genres", "actors")


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()
    cinema_hall = serializers.StringRelatedField()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
