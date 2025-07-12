from rest_framework import serializers

from cinema.models import CinemaHall, Movie, Genre, MovieSession, Actor


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name",
                  "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows",
                  "seats_in_row", "capacity"]


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration",
                  "genres", "actors"]

    def get_actors(self, obj):
        return [f"{a.first_name} {a.last_name}" for a in obj.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description",
                  "duration", "genres", "actors"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name",
                                             read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title",
                  "cinema_hall_name", "cinema_hall_capacity"]


class MovieInSessionSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration",
                  "genres", "actors"]

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieInSessionSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    movie_id = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all(), source="movie", write_only=True
    )
    cinema_hall_id = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all(),
        source="cinema_hall",
        write_only=True
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie",
            "cinema_hall",
            "movie_id",
            "cinema_hall_id",
        ]


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["movie", "cinema_hall", "show_time"]


class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
