# write serializers here
from rest_framework import serializers
from .models import Genre, CinemaHall, Actor, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()
        ]


class MovieRetrieveSerializer(MovieSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.SlugRelatedField(
        source="movie", many=False, read_only=True, slug_field="title"
    )
    cinema_hall_name = serializers.SlugRelatedField(
        source="cinema_hall", many=False, read_only=True, slug_field="name"
    )
    cinema_hall_capacity = serializers.SlugRelatedField(
        source="cinema_hall", many=False, read_only=True, slug_field="capacity"
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


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)
