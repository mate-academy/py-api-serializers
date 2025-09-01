# write serializers here
from rest_framework import serializers

from cinema.models import Genre, CinemaHall, Actor, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieForMovieSessionDetailSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=False)
    cinema_hall = CinemaHallSerializer(many=False)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieForMovieSessionDetailSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ["id", "show_time",
                  "movie_title", "cinema_hall_name",
                  "cinema_hall_capacity"]
