from rest_framework import serializers
from .models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity"
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        )

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj):
        return [actor.full_name for actor in obj.actors.all()]


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
            "actors"
        )


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
            "cinema_hall_capacity"
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
