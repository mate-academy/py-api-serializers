from rest_framework import serializers
from cinema.models import CinemaHall, Actor, Genre, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = "__all__"


class CinemaHallDetailSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time",
                  "movie_title", "cinema_hall_name",
                  "cinema_hall_capacity")

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.seats_in_row * obj.cinema_hall.rows


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallDetailSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"
