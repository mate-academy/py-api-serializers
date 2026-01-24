from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession

class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"

class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class MovieListSerializer(serializers.ModelSerializer):
    # Requisito: genres como lista de strings (nomes)
    genres = serializers.StringRelatedField(many=True, read_only=True)
    # Requisito: actors como lista de strings (nome completo)
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, obj):
        # Retorna o full_name de cada ator
        return [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]

class MovieDetailSerializer(serializers.ModelSerializer):
    # Requisito: genres como objetos completos
    genres = GenreSerializer(many=True, read_only=True)
    # Requisito: actors como objetos completos
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"

class MovieSessionListSerializer(serializers.ModelSerializer):
    # Requisito: Campos derivados do movie e cinema_hall
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

class MovieSessionDetailSerializer(serializers.ModelSerializer):
    # Requisito: movie com informação completa (usando MovieDetailSerializer)
    movie = MovieDetailSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = "__all__"
