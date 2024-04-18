from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "movie", "cinema_hall", "show_time"]

    def get_genres(self, obj):
        return obj.movie.genres.all().values_list("name", flat=True)

    def get_actors(self, obj):
        actor = obj.movie.actors.all().values_list("first_name", "last_name")
        actors = (
            [f"{first_name} "
             f"{last_name}" for first_name,
             last_name in actor]
        )
        return actors


class MovieSerializer(serializers.ModelSerializer):
    sessions = MovieSessionSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
            "sessions"
        )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        ]


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieRetrieveSerializer(MovieSessionSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
