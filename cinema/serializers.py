from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row", "capacity"]


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    full_name = serializers.SlugRelatedField(
        read_only=True,
        slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
            "full_name"]


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        ]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
