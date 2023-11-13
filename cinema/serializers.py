from rest_framework import serializers

from cinema.models import (Genre,
                           Movie,
                           Actor,
                           CinemaHall,
                           MovieSession
                           )


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model: Actor
        fields = ("first_name", "Last_name")


class GenreSerializer(serializers.Serializer):

    class Meta:
        model = Genre
        fields = "name"


class CinemaHallSerializer(serializers.Serializer):

    class Meta:
        model: CinemaHall
        fields = ("name", "rows", "seats_in_row")


class MovieSerializer(serializers.Serializer):
    class Meta:
        model: Movie
        fields = ("title", "description", "duration", "genres", "actors")



class MovieSessionSerializer(serializers.Serializer):
    class Meta:
        model: Movie
        fields = ("show_time", "movie", "cinema_hall")
