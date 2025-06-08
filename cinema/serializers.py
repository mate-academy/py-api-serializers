from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", "id")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Actor
        fields = (
            "id", "full_name",
        )
    def get_full_name(self, obj):
        return obj.full_name

class ActorListSerializer(ActorSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
        )


class CinemaHallListSerializer(CinemaHallSerializer):
    class Meta:
        model = CinemaHall


class CinemaHallRetrieveSerializer(CinemaHallSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        )


class MovieSerializer(serializers.ModelSerializer):
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


class MovieListSerializer(MovieSerializer):
    actors = serializers.SerializerMethodField()
    genres = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    def get_actors(selfself, obj):
        return [actor.full_name for actor in obj.actors.all()]

    class Meta(MovieSerializer.Meta):
        pass


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorListSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta(MovieSessionSerializer.Meta):
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionRetrieveSerializer(MovieSessionListSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallRetrieveSerializer(read_only=True)

    class Meta(MovieSessionListSerializer.Meta):
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "movie", "cinema_hall", "show_time"]
