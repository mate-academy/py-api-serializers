from rest_framework import serializers

from cinema.models import (Actor,
                           Movie,
                           CinemaHall,
                           Genre,
                           Ticket,
                           MovieSession)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True, slug_field="name", read_only=True)
    actors = serializers.StringRelatedField(many=True)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time",
                  "movie",
                  "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.SerializerMethodField()

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.rows * obj.cinema_hall.seats_in_row

    class Meta:
        model = MovieSession
        fields = ("id", "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")


class ActorDetailSerializer(ActorSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorDetailSerializer(many=True)


class CinemaHallDetailSerializer(CinemaHallSerializer):
    capacity = serializers.SerializerMethodField()

    def get_capacity(self, obj):
        return obj.rows * obj.seats_in_row

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(many=False)
    cinema_hall = CinemaHallDetailSerializer(many=False)
