from rest_framework import serializers

from cinema.models import CinemaHall, MovieSession, Movie, Actor, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(
        many=True,
        read_only=True,
    )
    actors = ActorSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(MovieSessionSerializer):
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity")
    cinema_hall_name = serializers.CharField(max_length=255, source="cinema_hall.name")
    movie_title = serializers.CharField(max_length=255, source="movie.title")

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        ]
