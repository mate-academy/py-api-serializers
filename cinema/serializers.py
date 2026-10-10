from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class ActorListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "full_name"]


class NestedPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer_class = kwargs.pop("serializer_class")
        super().__init__(**kwargs)

    def to_representation(self, value):
        return self.serializer_class(value, context=self.context).data

    def use_pk_only_optimization(self):
        return False


class MovieSerializer(serializers.ModelSerializer):
    genres = NestedPrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        serializer_class=GenreSerializer,
    )
    actors = NestedPrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all(),
        serializer_class=ActorSerializer,
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
        ]


class MovieListSerializer(serializers.ModelSerializer):
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


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = NestedPrimaryKeyRelatedField(
        queryset=Movie.objects.all(),
        serializer_class=MovieListSerializer,
    )
    cinema_hall = NestedPrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        serializer_class=CinemaHallSerializer,
    )

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True,
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True,
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
