from rest_framework import serializers
from cinema.models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession
)


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


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.ReadOnlyField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj):
        return [genre.name for genre in obj.genres.all()]

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()
                ]


class MovieCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("The title cannot be blank.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Duration must be a positive integer."
            )
        return value


class MovieDetailSerializer(MovieListSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
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


class MovieSessionDetailSerializer(MovieSessionListSerializer):
    movie = serializers.SerializerMethodField()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        )

    def get_movie(self, obj):
        return {
            "id": obj.movie.id,
            "title": obj.movie.title,
            "description": obj.movie.description,
            "duration": obj.movie.duration,
            "genres": [genre.name for genre in obj.movie.genres.all()],
            "actors": [f"{actor.first_name} {actor.last_name}"
                       for actor in obj.movie.actors.all()
                       ]
        }


class MovieSessionCreateSerializer(MovieSessionListSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

    def create(self, validated_data):
        return MovieSession.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get(
            "show_time", instance.show_time
        )
        instance.movie = validated_data.get("movie", instance.movie)
        instance.cinema_hall = validated_data.get(
            "cinema_hall", instance.cinema_hall
        )
        instance.save()
        return instance
