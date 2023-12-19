from rest_framework import serializers

from cinema.models import (Genre,
                           MovieSession,
                           Movie,
                           CinemaHall,
                           Actor)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ("id",
                  "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True, many=False)
    cinema_hall = CinemaHallSerializer(read_only=True, many=False)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
