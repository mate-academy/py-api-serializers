from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class ActorDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class CinemaHallDetailSerializer(serializers.ModelSerializer):
    cinema_hall_capacity = serializers.IntegerField(
        source="capacity", read_only=True
    )

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "cinema_hall_capacity")


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres"
        )


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.StringRelatedField(
        many=True,
    )


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorDetailSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True, many=False)
    cinema_hall = CinemaHallDetailSerializer(read_only=True, many=False)
