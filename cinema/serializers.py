from rest_framework import serializers

from cinema.models import Genre, Movie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        ]


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )

class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)