from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", )


class GenreListSerializer(GenreSerializer):

    class Meta:
        model = Genre
        fields = GenreSerializer.Meta.fields


class GenreRetrieveSerializer(GenreSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name", )


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name", )


class ActorRetrieveSerializer(ActorSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name", )


class ActorListSerializer(ActorSerializer):
    class Meta:
        model = Actor
        fields = ("full_name", )


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity", )
        read_only_fields = ("id", )


class CinemaHallListSerializer(CinemaHallSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity", )


class CinemaHallRetrieveSerializer(CinemaHallSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity", )


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ("id", "title",
                  "description",
                  "duration", "genres",
                  "actors", )
        read_only_fields = ("id", )


class MovieListSerializer(MovieSerializer):
    genres = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="name")
    actors = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="full_name")


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreRetrieveSerializer(many=True, read_only=True)
    actors = ActorRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title",
                  "description", "duration",
                  "genres", "actors", )


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", )
        read_only_fields = ("id", )


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title",
                                        read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name",
                                             read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity",
        read_only=True
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time",
                  "movie_title", "cinema_hall_name",
                  "cinema_hall_capacity", )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallListSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall", )
