# write serializers here
from rest_framework import serializers

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = [
            "id",
            "name",
        ]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
        ]

    def get_full_name(self, obj):
        return str(obj)


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = [
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        ]


class BaseMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSerializer(BaseMovieSerializer):
    pass


class MovieListSerializer(BaseMovieSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)


class MovieRetrieveSerializer(BaseMovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class BaseMovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
        ]


class MovieSessionSerializer(BaseMovieSessionSerializer):
    class Meta(BaseMovieSessionSerializer.Meta):
        fields = BaseMovieSessionSerializer.Meta.fields + [
            "movie",
            "cinema_hall",
        ]


class MovieSessionListSerializer(BaseMovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta(BaseMovieSessionSerializer.Meta):
        fields = BaseMovieSessionSerializer.Meta.fields + [
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]


class MovieSessionRetrieveSerializer(BaseMovieSessionSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)

    class Meta(BaseMovieSessionSerializer.Meta):
        fields = BaseMovieSessionSerializer.Meta.fields + [
            "movie",
            "cinema_hall",
        ]
