from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", queryset=Genre.objects.all()
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "__all__"

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title")
    cinema_hall_name = serializers.ReadOnlyField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.ReadOnlyField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]
