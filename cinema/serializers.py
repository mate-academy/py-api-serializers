from rest_framework import serializers

from cinema.models import CinemaHall


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = (
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )
