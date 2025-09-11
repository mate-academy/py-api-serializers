from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, actor: Actor):
        return f"{actor.first_name} {actor.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )

    actors = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, movie: Movie):
        return [f"{a.first_name} {a.last_name}" for a in movie.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieWriteSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def create(self, validated_data):
        genres = validated_data.pop("genres", [])
        actors = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        if genres:
            movie.genres.set(genres)
        if actors:
            movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop("genres", None)
        actors = validated_data.pop("actors", None)

        for item, value in validated_data.items():
            setattr(instance, item, value)
        instance.save()

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)
        return instance


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id",
                  "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
