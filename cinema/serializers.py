from rest_framework import serializers

from cinema.models import (
    Movie,
    Genre,
    Actor,
    CinemaHall,
    MovieSession,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name",)


class ActorListSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(method_name="get_full_name")

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name",)


class ActorDetailSerializer(ActorSerializer):
    full_name = serializers.SerializerMethodField(method_name="get_full_name")

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name",)

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieDetailSerializer(MovieListSerializer):
    actors = ActorDetailSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity",)


class MovieSessionSerializer(serializers.ModelSerializer):

    movie_title = serializers.SlugRelatedField(
        slug_field="title",
        read_only=True,
        source="movie"
    )
    cinema_hall_name = serializers.SlugRelatedField(
        slug_field="name",
        read_only=True,
        source="cinema_hall"
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
            "cinema_hall_capacity",
        )


class MovieSessionCreateSerializer(MovieSessionSerializer):
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects
    )
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "movie_title",
            "cinema_hall",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )
