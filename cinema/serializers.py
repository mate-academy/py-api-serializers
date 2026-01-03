from rest_framework import serializers

from cinema.models import (
    Genre,
    Actor,
    Movie, CinemaHall, MovieSession,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name",)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    # Accept actor IDs for POST, display names for GET
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def to_representation(self, instance) -> dict:
        """Customize output: display names for list view"""
        rep = super().to_representation(instance)
        rep["genres"] = [genre.name for genre in instance.genres.all()]
        rep["actors"] = [f"{a.first_name} {a.last_name}"
                         for a in instance.actors.all()]
        return rep


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    cinema_hall_name = serializers.SerializerMethodField()
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

    def get_movie_title(self, obj) -> int:
        return obj.movie.title if obj.movie else None

    def get_cinema_hall_name(self, obj) -> int:
        return obj.cinema_hall.name if obj.cinema_hall else None

    def get_cinema_hall_capacity(self, obj) -> int | None:
        if obj.cinema_hall:
            seats_in_row = obj.cinema_hall.seats_in_row
            rows = obj.cinema_hall.rows
            return seats_in_row * rows
        else:
            return None


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

    def to_representation(self, instance) -> dict:
        # Start with the default representation
        rep = super().to_representation(instance)

        # Add capacity inside cinema_hall
        if instance.cinema_hall:
            rep["cinema_hall"]["capacity"] = (
                instance.cinema_hall.rows * instance.cinema_hall.seats_in_row
            )

        return rep
