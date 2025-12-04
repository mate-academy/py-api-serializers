from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ('id', 'first_name', 'last_name', 'full_name')

    def get_full_name(self, obj) -> str:
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ('id', 'name', 'rows', 'seats_in_row', 'capacity')


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Genre.objects.all())
    actors = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'genres', 'actors')


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field='name')
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", 'show_time', 'movie', 'cinema_hall')


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.ReadOnlyField(source="movie.title",
                                            read_only=True)
    cinema_hall_name = serializers.ReadOnlyField(source="cinema_hall.name",
                                                 read_only=True)
    cinema_hall_capacity = serializers.SerializerMethodField()

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )

    def get_cinema_hall_capacity(self, obj) -> int:
        return obj.cinema_hall.capacity


class MovieSessionDetailSerializer(MovieSessionListSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ('id', 'show_time', 'movie', 'cinema_hall')
