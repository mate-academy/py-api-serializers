from rest_framework import serializers
from rest_framework.relations import (
    SlugRelatedField,
    StringRelatedField
)

from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name",
        )

    def get_full_name(self, obj):
        return str(obj)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
        )


class CinemaHallDetailSerializer(CinemaHallSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta(CinemaHallSerializer.Meta):
        fields = CinemaHallSerializer.Meta.fields + ("capacity",)

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


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
    genres = SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = StringRelatedField(
        many=True,
        read_only=True,
    )


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ("genres", "actors")


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
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.rows * obj.cinema_hall.seats_in_row


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallDetailSerializer()

    class Meta(MovieSessionSerializer.Meta):
        fields = MovieSessionSerializer.Meta.fields + ("movie", "cinema_hall")
