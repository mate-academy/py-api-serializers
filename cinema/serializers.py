from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, CinemaHall, MovieSession


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", read_only=True
    )
    actors = serializers.StringRelatedField(many=True, read_only=True)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.SerializerMethodField()
    cinema_hall_name = serializers.SerializerMethodField()
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = ("id",
                  "show_time",
                  "movie",
                  "cinema_hall",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")

    def get_movie_title(self, obj):
        return obj.movie.title

    def get_cinema_hall_name(self, obj):
        return obj.cinema_hall.name

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.capacity
