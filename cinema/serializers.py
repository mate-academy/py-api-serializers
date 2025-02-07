from rest_framework import serializers
from django.contrib.auth import get_user_model
from cinema.models import (
    Genre, Actor, Movie,
    CinemaHall, MovieSession,
    Ticket, Order
)

User = get_user_model()


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieDetailSerializer(serializers.ModelSerializer):

    genres = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="name")
    actors = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="full_name")

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class CinemaHallListSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class CinemaHallDetailSerializer(serializers.ModelSerializer):
    # capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = [
            "id", "show_time", "movie_title",
            "cinema_hall_name", "cinema_hall_capacity"
        ]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer()
    cinema_hall = CinemaHallDetailSerializer()
    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), write_only=True, source="movie"
    )
    cinema_hall_id = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        write_only=True, source="cinema_hall"
    )

    class Meta:
        model = MovieSession
        fields = "__all__"
        # fields = [
        #     "id", "show_time", "movie", "cinema_hall",
        #     "movie_id", "cinema_hall_id"
        # ]

    def create(self, validated_data):
        return MovieSession.objects.create(**validated_data)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieCreateSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)
