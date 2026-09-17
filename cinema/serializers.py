from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer,):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        required=False
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        required=False
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
    )
    movie_title = serializers.ReadOnlyField(
        source="movie.title"
    )

    cinema_hall_name = serializers.ReadOnlyField(
        source="cinema_hall.name"
    )
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = ("id",
                  "movie",
                  "show_time",
                  "movie_title",
                  "cinema_hall",
                  "cinema_hall_name",
                  "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(
        source="movie.title"
    )

    cinema_hall_name = serializers.ReadOnlyField(
        source="cinema_hall.name"
    )
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = ("id",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")
