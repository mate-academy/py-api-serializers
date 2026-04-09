from rest_framework import serializers


from cinema.models import (Genre,
                           Actor,
                           CinemaHall,
                           Movie,
                           MovieSession)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieListSerializer(serializers.ModelSerializer):

    genres = serializers.SlugRelatedField(many=True, read_only=True,
                                          slug_field="name")
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_actors(self, obj) -> list[str]:
        return [f"{a.first_name} {a.last_name}" for a in obj.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieCreateSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all())

    def create(self, validated_data) -> Movie:
        genres = validated_data.pop("genres", [])
        actors = validated_data.pop("actors", [])
        movie = Movie.objects.create(**validated_data)
        movie.genres.set(genres)
        movie.actors.set(actors)
        return movie

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SlugRelatedField(
        source="movie",
        many=False,
        read_only=True,
        slug_field="title")
    cinema_hall_name = serializers.SlugRelatedField(
        source="cinema_hall",
        many=False,
        read_only=True,
        slug_field="name")

    cinema_hall_capacity = serializers.SlugRelatedField(
        source="cinema_hall",
        many=False,
        read_only=True,
        slug_field="capacity")

    class Meta:
        model = MovieSession
        fields = ("id",
                  "show_time",
                  "movie_title",
                  "cinema_hall_name",
                  "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):

    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all())
    movie = serializers.PrimaryKeyRelatedField(
        queryset=Movie.objects.all())

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
