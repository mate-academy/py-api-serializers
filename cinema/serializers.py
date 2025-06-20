from django.utils import timezone

from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ["id",
                  "title",
                  "description",
                  "duration",
                  "genres",
                  "actors"]
        extra_kwargs = {
            "duration": {"min_value": 1, "max_value": 500},
            "title": {"required": True, "max_length": 255},
            "description": {"required": True},
        }

    def validate(self, data):
        if "actors" in data:
            non_existent_actors = \
                (set(data["actors"]) - set(Actor.objects.values_list(
                    "id",
                    flat=True)))
            if non_existent_actors:
                raise serializers.ValidationError(
                    {"actors":
                     f"Actors with IDs {non_existent_actors} do not exist."}
                )

        if "genres" in data:
            non_existent_genres = \
                (set(data["genres"]) - set(Genre.objects.values_list(
                    "id",
                    flat=True)))
            if non_existent_genres:
                raise serializers.ValidationError(
                    {"genres":
                     f"Genres with IDs {non_existent_genres} do not exist."}
                )

        if "duration" in data and data["duration"] <= 0:
            raise serializers.ValidationError(
                {"duration": "Duration must be a positive number."}
            )

        if "title" in data and not data["title"].strip():
            raise serializers.ValidationError(
                {"title": "Title cannot be empty."}
            )

        return data


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id",
                  "title",
                  "description",
                  "duration",
                  "genres",
                  "actors"]

    def get_actors(self, obj):
        return sorted([f"{actor.first_name} {actor.last_name}"
                       for actor in obj.actors.all()])


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        source="movie",
        write_only=True
    )
    cinema_hall_id = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        source="cinema_hall",
        write_only=True
    )

    class Meta:
        model = MovieSession
        fields = [
            "id", "show_time", "movie", "cinema_hall",
            "movie_id", "cinema_hall_id"
        ]

    def validate(self, data):
        if "show_time" in data and data["show_time"] < timezone.now():
            raise serializers.ValidationError(
                {"show_time": "Show time must be in the future."}
            )
        return data

    def create(self, validated_data):
        required_fields = ["movie", "cinema_hall", "show_time"]
        for field in required_fields:
            if field not in validated_data:
                raise serializers.ValidationError(
                    {field: "This field is required."}
                )

        return super().create(validated_data)


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title",
                                        read_only=True)
    movie_genres = serializers.SerializerMethodField()
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True)
    show_time = serializers.DateTimeField()

    class Meta:
        model = MovieSession
        fields = [
            "id", "show_time", "movie_title", "movie_genres",
            "cinema_hall_name", "cinema_hall_capacity"
        ]

    def get_movie_genres(self, obj):
        return sorted([genre.name for genre in obj.movie.genres.all()])
