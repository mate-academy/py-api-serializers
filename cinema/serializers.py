
from rest_framework import serializers

from .models import CinemaHall, Genre, Actor, Movie, MovieSession


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj: Actor) -> str:
        return f'{obj.first_name} {obj.last_name}'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many=True)
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieUpdateSerializer(MovieSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj: Movie) -> list[str]:
        return [f'{actor.first_name} {actor.last_name}' for actor in obj.actors.all()]

class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie', 'cinema_hall']

class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(
        source='movie.title',
        read_only= True
    )
    cinema_hall_name = serializers.CharField(
        source='cinema_hall.name',
        read_only=True
    )

    cinema_hall_capacity = serializers.IntegerField(
        source='cinema_hall.capacity'
    )
    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie_title', 'cinema_hall_name', 'cinema_hall_capacity']

class MovieSessionUpdateSerializer(MovieSessionSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(queryset=CinemaHall.objects.all())
    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie', 'cinema_hall']