from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


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
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]
        read_only_fields = ["id", "capacity"]


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
        read_only_fields = ["id"]

    def get_actors(self, obj):
        result = []
        for actor in obj.actors.all():
            result.append(f"{actor.first_name} {actor.last_name}")
        return result


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
        read_only_fields = ["id"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
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
        fields = ["id", "show_time", "movie_title",
                  "cinema_hall_name", "cinema_hall_capacity"]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ["id"]
