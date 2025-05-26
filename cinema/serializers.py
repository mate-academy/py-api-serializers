from rest_framework import serializers
from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


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
    capacity = serializers.IntegerField(read_only=True)

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
                for actor in obj.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta(MovieListSerializer.Meta):
        fields = MovieListSerializer.Meta.fields


class MovieWriteSerializer(serializers.ModelSerializer):
    genres = (
        serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(),
                                           many=True))
    actors = (
        serializers.PrimaryKeyRelatedField(queryset=Actor.objects.all(),
                                           many=True))

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "genres", "actors")

    def create(self, validated_data):
        genres = validated_data.pop("genres")
        actors = validated_data.pop("actors")
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        movie.actors.set(actors)
        return movie

    def update(self, instance, validated_data):
        genres = validated_data.pop("genres", None)
        actors = validated_data.pop("actors", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)

        instance.save()
        return instance


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = (
        serializers.CharField(source="movie.title"))
    cinema_hall_name = (
        serializers.CharField(source="cinema_hall.name"))
    cinema_hall_capacity = (
        serializers.IntegerField(source="cinema_hall.capacity"))

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionWriteSerializer(serializers.ModelSerializer):
    movie = (
        serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all()))
    cinema_hall = (
        serializers.PrimaryKeyRelatedField(queryset=CinemaHall.objects.all()))

    class Meta:
        model = MovieSession
        fields = ("show_time", "movie", "cinema_hall")
