from rest_framework import serializers

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True, source="__str__")

    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )
        read_only_fields = ("id",)


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True, source="genres.all")
    actors = serializers.StringRelatedField(many=True, source="actors.all")

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


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", required=False, read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", required=False, read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        required=False,
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
