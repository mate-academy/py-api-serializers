from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession


class GenreSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)


class MovieDetailSerialiser(MovieSerializer):
    actors = ActorSerialiser(many=True, read_only=True)
    genres = GenreSerialiser(many=True, read_only=True)


class CinemaHallSerialiser(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class MovieSessionSerialiser(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(MovieSessionSerialiser):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name",
                                             read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title",
                  "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerialiser(MovieSessionSerialiser):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerialiser(read_only=True)
