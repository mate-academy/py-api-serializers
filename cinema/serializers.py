from rest_framework import serializers

from cinema.models import (Actor,
                           CinemaHall,
                           Genre,
                           Movie,
                           MovieSession)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    def get_actors(self, obj):
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()

    def get_movie_title(self, obj):
        return f"{obj.movie.title}"

    cinema_hall_name = serializers.SerializerMethodField()

    def get_cinema_hall_name(self, obj):
        return f"{obj.cinema_hall.name}"

    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
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
    cinema_hall = CinemaHallSerializer(read_only=True)
    movie = serializers.SerializerMethodField()

    def get_movie(self, obj):
        return {
            "id": obj.movie.id,
            "title": obj.movie.title,
            "description": obj.movie.description,
            "duration": obj.movie.duration,
            "genres": [genre.name for genre in obj.movie.genres.all()],
            "actors": [
                f"{actor.first_name} {actor.last_name}"
                for actor in obj.movie.actors.all()
            ]
        }

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
