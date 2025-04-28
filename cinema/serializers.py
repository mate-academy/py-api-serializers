from rest_framework import serializers

from cinema.models import Actor, Genre, CinemaHall, Movie, MovieSession


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("full_name",)


class ActorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name",)


class GenreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class CinemaHallListSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ("name", "rows", "seats_in_row", "capacity")

    def get_capacity(self, obj):
        return obj.capacity


class CinemaHallDetailSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")

    def get_capacity(self, obj):
        return obj.capacity


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = ActorDetailSerializer(many=True, read_only=True)
    genres = GenreDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "actors", "genres")


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "actors", "genres")

    def get_actors(self, obj):
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]

    def get_genres(self, obj):
        return [f"{genre.name}" for genre in obj.genres.all()]


class MovieCreateSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = ("title", "description", "duration", "actors", "genres")


class MovieSessionListSerializer(serializers.ModelSerializer):
    # show_time = serializers.DateTimeField()
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ("movie_title", "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallDetailSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(
        queryset=CinemaHall.objects.all()
    )

    class Meta:
        model = MovieSession
        fields = ("movie", "show_time", "cinema_hall")
