from rest_framework import serializers

from cinema.models import Movie, CinemaHall, Actor, Genre, MovieSession


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.ModelSerializer):
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
            "cinema_hall_capacity",
        ]


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieRetrieveSerializer(MovieSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)


class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
