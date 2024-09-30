from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField(method_name="get_actors")

    class Meta:
        model = Movie
        fields = "__all__"

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class ActorForMovieRetrieveSerializer(ActorSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieRetrieveSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorForMovieRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"

    def validate(self, data):
        if not data.get("cinema_hall"):
            raise serializers.ValidationError(
                {"cinema_hall": "Cinema hall is required"}
            )
        return data


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
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


class MovieForMovieSessionRetrieveSerializer(MovieSessionSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="full_name"
    )

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieForMovieSessionRetrieveSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
