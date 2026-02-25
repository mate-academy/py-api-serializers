# write serializers here
from rest_framework import serializers

from cinema.models import CinemaHall, Genre


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]