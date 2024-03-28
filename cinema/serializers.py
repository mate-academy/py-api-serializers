from rest_framework import serializers

from cinema.models import Movie, Actor, Genre


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("first_name", "last_name")


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenresSerializer(many=True)

    class Meta:
        model = Movie
        fields = ('title', 'description', 'duration', 'genres', 'actors')
