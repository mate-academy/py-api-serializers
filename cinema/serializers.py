from rest_framework import serializers
from cinema.models import (
    Order,
    Ticket,
    CinemaHall,
    Actor,
    Genre,
    Movie,
    MovieSession
)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row")


class CinemaHallDetailSerializer(serializers.ModelSerializer):
    def get_capacity(self, obj):
        return obj.capacity

    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ("movie_title", "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()
    cinema_hall = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

    def get_movie(self, obj):
        movie = obj.movie
        return {
            "id": movie.id,
            "title": movie.title,
            "description": movie.description,
            "duration": movie.duration,
            "genres": [genre.name for genre in movie.genres.all()],
            "actors": [
                f"{actor.first_name} {actor.last_name}"
                for actor in movie.actors.all()
            ],
        }

    def get_cinema_hall(self, obj):
        cinema_hall = obj.cinema_hall
        return {
            "id": cinema_hall.id,
            "name": cinema_hall.name,
            "rows": cinema_hall.rows,
            "seats_in_row": cinema_hall.seats_in_row,
            "capacity": cinema_hall.capacity
        }


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
