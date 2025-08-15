# write serializers here
from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )
        read_only_fields = ("id",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")
        read_only_fields = ("id",)


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
        read_only_fields = ("id",)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")
        read_only_fields = ("id",)


class DetailCinemaHallSerializer(
    CinemaHallSerializer
):
    class Meta:
        model = CinemaHall
        fields = (CinemaHallSerializer.Meta.fields + ("capacity",))


class ListMovieSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field="name",
        many=True
    )
    actors = serializers.SlugRelatedField(
        queryset=Actor.objects.all(),
        slug_field="full_name",
        many=True
    )

    class Meta:
        model = Movie
        fields = (MovieSerializer.Meta.fields + ("genres", "actors"))


class DetailMovieSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = (MovieSerializer.Meta.fields + ("genres", "actors"))


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )


class ListMovieSessionSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class DetailMovieSessionSerializer(MovieSessionSerializer):
    movie = ListMovieSerializer(many=False, required=False)
    cinema_hall = DetailCinemaHallSerializer(
        many=False,
        required=False
    )

    class Meta:
        model = MovieSession
        fields = MovieSessionSerializer.Meta.fields + (
            "movie",
            "cinema_hall",
        )
