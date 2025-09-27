from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only_fields = ["id"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]
        read_only_fields = ["id"]

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]
        read_only_fields = ["id"]

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True, queryset=Actor.objects.all())
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
        read_only_fields = ["id"]


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}" for actor in obj.actors.all()]


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ["id"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity"]

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.rows * obj.cinema_hall.seats_in_row


class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
        read_only_fields = ["id"]
