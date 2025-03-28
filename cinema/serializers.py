# write serializers here
from rest_framework import serializers
from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    actors = serializers.SlugRelatedField(many=True, read_only=True, slug_field="first_name")

class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSessionSerializer(serializers.ModelSerializer):
    cinema_hall_name = serializers.SerializerMethodField()
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall_name", "cinema_hall_capacity")

    def get_cinema_hall_name(self, obj):
        return obj.cinema_hall.name

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.seats_in_row * obj.cinema_hall.rows

class MovieSessionListSerializer(MovieSessionSerializer):
    movie = serializers.SlugRelatedField(read_only=True, slug_field="title")


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieRetrieveSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta(MovieSessionSerializer.Meta):
        fields = MovieSessionSerializer.Meta.fields + ("cinema_hall",)


