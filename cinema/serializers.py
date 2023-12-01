from rest_framework import serializers

from cinema.models import (Genre,
                           Actor,
                           CinemaHall,
                           Movie,
                           MovieSession)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class ActorFullNameSlugRelatedField(serializers.SlugRelatedField):
    def __init__(self, slug_field=None, **kwargs) -> None:
        super().__init__(slug_field=slug_field, **kwargs)

    def to_representation(self, actor: Actor) -> str:
        return f"{actor.first_name} {actor.last_name}"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    @staticmethod
    def get_full_name(actor: Actor) -> str:
        return f"{actor.first_name} {actor.last_name}"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = ActorFullNameSlugRelatedField(
        many=True,
        read_only=True,
        slug_field="full_name"
    )


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(read_only=False, many=True)
    actors = ActorSerializer(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True, many=False)
    cinema_hall = CinemaHallSerializer(read_only=True, many=False)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall"
        )
