from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Actor,
    Genre,
    Movie,
    MovieSession,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    def get_full_name(self, obj):
        return str(obj)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name")
    actors = serializers.StringRelatedField(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False)
    cinema_hall = CinemaHallSerializer(many=False)


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(read_only=True, source="movie.title")
    cinema_hall_name = serializers.CharField(
        read_only=True, source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        read_only=True, source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title",
                  "cinema_hall_name", "cinema_hall_capacity")
