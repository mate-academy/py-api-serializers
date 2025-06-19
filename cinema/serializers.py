from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
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
        fields = ["id",
                  "title",
                  "description",
                  "duration",
                  "genres",
                  "actors"]

    def create(self, validated_data):
        genres_data = validated_data.pop("genres")
        actors_data = validated_data.pop("actors")
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres_data)
        movie.actors.set(actors_data)
        return movie

    def update(self, instance, validated_data):
        genres_data = validated_data.pop("genres", None)
        actors_data = validated_data.pop("actors", None)

        instance.title = validated_data.get("title",
                                            instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.duration = validated_data.get("duration",
                                               instance.duration)
        instance.save()

        if genres_data is not None:
            instance.genres.set(genres_data)
        if actors_data is not None:
            instance.actors.set(actors_data)

        return instance


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]


class MovieSessionSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]

    def create(self, validated_data):
        return MovieSession.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get("show_time",
                                                instance.show_time)
        instance.movie = validated_data.get("movie",
                                            instance.movie)
        instance.cinema_hall = validated_data.get("cinema_hall",
                                                  instance.cinema_hall)
        instance.save()
        return instance


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title",
                                        read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True)
    show_time = serializers.DateTimeField()

    class Meta:
        model = MovieSession
        fields = ["id",
                  "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity"]
