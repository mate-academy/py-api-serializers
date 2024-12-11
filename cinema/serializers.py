from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name",)


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = (
            "first_name",
            "last_name",
            "full_name",
        )


class ActorDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    actors = serializers.StringRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreDetailSerializer(many=True, read_only=True)
    actors = ActorDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.SlugRelatedField(
        slug_field="title",
        source="movie",
        read_only=True
    )
    cinema_hall_name = serializers.SlugRelatedField(
        slug_field="name",
        source="cinema_hall",
        read_only=True
    )
    cinema_hall_capacity = serializers.SlugRelatedField(
        slug_field="capacity",
        source="cinema_hall",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
            "cinema_hall",
            "movie",
        )
        read_only_fields = ("id",)


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )
