from rest_framework import serializers

from cinema.models import Genre, Actor


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("name", )

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("first_name", "last_name", "full_name")