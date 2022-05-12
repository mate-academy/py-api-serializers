from rest_framework import serializers

from cinema.models import Genre


class GenreSerializers(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name", )

