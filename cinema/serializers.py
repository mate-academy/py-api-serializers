from rest_framework import serializers
from rest_framework.relations import SlugRelatedField, StringRelatedField
from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


# ----------------------------------------------------------------------------


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


# ----------------------------------------------------------------------------


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


# ----------------------------------------------------------------------------


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(MovieSerializer):
    actors = serializers.SlugRelatedField(slug_field="full_name", many=True, read_only=True)
    genres = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


# actors = serializers.SlugRelatedField(slug_field="full_name", many=True, read_only=True)
# genres = serializers.SlugRelatedField(slug_field="name", many=True, read_only=True)

# ----------------------------------------------------------------------------


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerializer(MovieSessionSerializer):
    cinema_hall = CinemaHallSerializer(read_only=True)
    show_time = serializers.DateTimeField(read_only=True)
    movie = MovieListSerializer()


# ----------------------------------------------------------------------------
