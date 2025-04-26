from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "actors", "genres")


class MovieListSerializer(MovieSerializer):
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


class MovieRetrieveSerializer(MovieSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieSRetrieveSerializer(MovieSerializer):

    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )

    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name",
    )


class MovieSessionSerializer(serializers.ModelSerializer):
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "movie_title",
            "cinema_hall",
            "cinema_hall_capacity",
            "cinema_hall_name"
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    cinema_hall = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="name"
    )
    movie = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="title"
    )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):

    cinema_hall = CinemaHallSerializer(many=False, read_only=True)
    movie = MovieSRetrieveSerializer(many=False, read_only=True)
