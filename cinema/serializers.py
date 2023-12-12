from rest_framework import serializers

from cinema.models import CinemaHall, Actor, Genre, Movie, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = "__all__"


class ActorDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorDetailSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"
