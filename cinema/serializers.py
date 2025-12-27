from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    """
    Model serializer for the CinemaHall entity
    """
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Genre entity
    """
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Actor entity
    """

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieSerializer(serializers.ModelSerializer):
    """
    Model serializer for the Movie entity
    """
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


class MovieListSerializer(MovieSerializer):
    """
    Serializer for retrieving a list of movies.

    Extends MovieSerializer to include read-only representations of
    related genres and actors. Genres are represented by their name field,
    while actors are represented using their string representation.
    """
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True
    )


class MovieRetrieveSerializer(MovieSerializer):
    """
    Serializer for retrieving detailed information of a single movie.

    Extends MovieSerializer to include full nested representations of
    related genres and actors using their respective serializers.
    Genres are represented with GenreSerializer, and actors with ActorSerializer.
    """
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    """
    Model serializer for the MovieSession entity
    """
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    """
    Serializer for retrieving a list of movies sessions.

    Extends MovieSessionSerializer to include read-only representations of
    related movie and cinema_hall. Movie are represented by their title field,
    while cinema_hall are represented using their name field.
    """

    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
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


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    """
    Serializer for retrieving detailed information of a single movie session.

    Extends MovieSerializer to include full nested representations of
    related movie and cinema_hall using their respective serializers.
    Movie are represented with MovieSerializer, and cinema_hall with CinemaHallSerializer.
    """

    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer()
