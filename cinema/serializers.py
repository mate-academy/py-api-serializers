from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


# ----- Simple serializers -----

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}".strip()


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class CinemaHallDetailSerializer(CinemaHallSerializer):
    capacity = serializers.SerializerMethodField(read_only=True)

    class Meta(CinemaHallSerializer.Meta):
        fields = CinemaHallSerializer.Meta.fields + ("capacity",)

    def get_capacity(self, obj) -> int:
        return int(obj.rows) * int(obj.seats_in_row)


# ----- Movie serializers (list/detail/write) -----

class MovieListSerializer(serializers.ModelSerializer):
    # list view: genres -> names, actors -> full names
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")

    def get_genres(self, obj):
        return [g.name for g in obj.genres.all()]

    def get_actors(self, obj):
        return [f"{a.first_name} {a.last_name}".strip()
                for a in obj.actors.all()]


class MovieDetailSerializer(serializers.ModelSerializer):
    # detail view: full info for genres & actors
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieWriteSerializer(serializers.ModelSerializer):
    # write with PK lists
    genres = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Genre.objects.all(), required=False
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Actor.objects.all(), required=False
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
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if genres is not None:
            instance.genres.set(genres)
        if actors is not None:
            instance.actors.set(actors)
        return instance


# ----- MovieSession serializers (list/detail/write) -----

class MovieSessionWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name",
                                             read_only=True)
    cinema_hall_capacity = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title",
                  "cinema_hall_name", "cinema_hall_capacity")

    def get_cinema_hall_capacity(self, obj) -> int:
        return int(obj.cinema_hall.rows) * int(obj.cinema_hall.seats_in_row)


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallDetailSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
