from rest_framework import serializers
from cinema.models import (
    CinemaHall,
    Genre,
    Actor,
    Movie,
    MovieSession,
    Order,
    Ticket,
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name', 'full_name']


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='full_name'
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'genres', 'actors']



class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)
    cinema_hall_name = serializers.CharField(source='cinema_hall.name', read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source='cinema_hall.capacity', read_only=True)

    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie_title', 'cinema_hall_name', 'cinema_hall_capacity']



class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ['id', 'show_time', 'movie', 'cinema_hall']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

