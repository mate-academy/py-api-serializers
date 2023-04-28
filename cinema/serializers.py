from rest_framework import serializers

from cinema.models import Movie, Genre, Actor


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors"
        )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(read_only=True, many=True)
    actors = ActorSerializer(read_only=True, many=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)
