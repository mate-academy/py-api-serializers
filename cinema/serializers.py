from rest_framework import serializers
from .models import CinemaHall, Genre, Actor, Movie, MovieSession, Order, Ticket


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
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = MovieSession
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionSerializer()
    order = OrderSerializer()

    class Meta:
        model = Ticket
        fields = "__all__"

