from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    hall_capacity = serializers.IntegerField(source="capacity", read_only=True)
    cinema_hall_name = serializers.CharField(source="name", read_only=True)

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "hall_capacity")


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=False, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = GenreListSerializer(many=False, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity", read_only=True)
