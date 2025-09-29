from typing import Any, Dict, List

from rest_framework import serializers

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}".strip()


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

    def get_capacity(self, obj: CinemaHall) -> int:
        return int(obj.rows) * int(obj.seats_in_row)


class MovieSerializer(serializers.ModelSerializer):
    """Base serializer for create/update with M2M writes handled."""

    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True
    )
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True
    )

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )

    def create(self, validated_data: Dict[str, Any]) -> Movie:
        genres = validated_data.pop("genres", [])
        actors = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        if genres:
            movie.genres.set(genres)
        if actors:
            movie.actors.set(actors)
        return movie

    def update(self, instance: Movie, validated_data: Dict[str, Any]) -> Movie:
        genres = validated_data.pop("genres", None)
        actors = validated_data.pop("actors", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)
        return instance


class MovieListSerializer(serializers.ModelSerializer):
    """List view: genres & actors as lists of strings."""

    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )
    actors = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )

    def get_actors(self, obj: Movie) -> List[str]:
        return [
            f"{a.first_name} {a.last_name}".strip()
            for a in obj.actors.all()
        ]


class MovieDetailSerializer(serializers.ModelSerializer):
    """Detail view: complete info about genres & actors."""

    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
        )


class MovieSessionSerializer(serializers.ModelSerializer):
    """Base serializer for create/update."""

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    """List view: flattened fields from related objects."""

    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

    def get_cinema_hall_capacity(self, obj: MovieSession) -> int:
        return int(obj.cinema_hall.rows) * int(obj.cinema_hall.seats_in_row)


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    """Detail view: complete info about the movie & cinema hall."""

    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
