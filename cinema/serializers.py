from rest_framework import serializers

from cinema.models import (
    CinemaHall,
    Actor,
    Movie,
    Genre,
    MovieSession
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)
