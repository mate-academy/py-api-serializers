# write serializers here
from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id","first_name","last_name","full_name")

class ActorDetailSerializer(ActorListSerializer):
    class Meta:
        model = Actor
        read_only_fields = ("full_name",)
        fields = ("id","first_name","last_name","full_name")

class CinemaHallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        read_only_fields = ("id",)
        fields = ("id","name","rows","seats_in_row","capacity")

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","title","description","duration","genres","actors")
class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(many=True,slug_field="name",read_only=True)
    actors = serializers.StringRelatedField(many=True,read_only=True)


class MovieDetailSerializer(MovieSerializer):
    genres = GenreListSerializer(many=True,read_only=True)
    actors = ActorDetailSerializer(many=True,read_only=True)

class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = ("id","show_time","movie_title","cinema_hall_name","cinema_hall_capacity")

class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False,read_only=True)
    cinema_hall = CinemaHallListSerializer(many=False,read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie","cinema_hall")