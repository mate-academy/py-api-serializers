from rest_framework import serializers
from .models import CinemaHall, Genre, Actor, Movie, MovieSession, Order, Ticket


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
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
