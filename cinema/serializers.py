from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cinema.models import CinemaHall, Genre, Actor, Movie, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()
        ]


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj):
        actors = ActorSerializer(obj.actors.all(), many=True).data
        for actor in actors:
            actor["full_name"] = f"{actor['first_name']} {actor['last_name']}"
        return actors


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    cinema_hall_name = serializers.CharField(source='cinema_hall.name', read_only=True)
    cinema_hall_capacity = serializers.CharField(source='cinema_hall.capacity', read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity",]


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
