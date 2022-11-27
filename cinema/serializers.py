from rest_framework import serializers

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = [
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        ]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
        ]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        ]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = [
            "id",
            "movie",
            "show_time",
            "cinema_hall",
        ]


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field="name",
    )
    actors = serializers.SlugRelatedField(
        read_only=True, many=True, slug_field="full_name"
    )


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)


class MovieSessionListSerializer(MovieSerializer):
    movie_title = serializers.CharField(
        read_only=True,
        source="movie.title",
    )
    cinema_hall_name = serializers.CharField(
        read_only=True,
        source="cinema_hall.name",
    )
    cinema_hall_capacity = serializers.IntegerField(
        read_only=True,
        source="cinema_hall.capacity",
    )

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
    cinema_hall = CinemaHallSerializer(read_only=True, many=False)
    movie = MovieListSerializer(read_only=True, many=False)
