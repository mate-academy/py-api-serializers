from rest_framework import serializers

from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            "id",
            "name",
        )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")
        read_only_fields = ("capacity",)


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionListSerializer(serializers.ModelSerializer):
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )
    movie_title = serializers.CharField(source="movie.title", read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"
