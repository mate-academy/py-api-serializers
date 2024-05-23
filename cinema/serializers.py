from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_actors(self, obj):
        return [actor.full_name for actor in obj.actors.all()]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title")
    cinema_hall_name = serializers.ReadOnlyField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]


class MovieSessionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
