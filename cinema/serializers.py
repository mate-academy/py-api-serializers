from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, MovieSession, CinemaHall


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class GenreRetrieveSerializer(GenreSerializer):
    pass


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class ActorRetrieveSerializer(ActorSerializer):
    pass


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(read_only=True, many=True)
    actors = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieRetrieveSerializer(MovieSerializer):
    genres = GenreRetrieveSerializer(many=True, read_only=True)
    actors = ActorRetrieveSerializer(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(read_only=True)
    cinema_hall_name = serializers.CharField(read_only=True)
    cinema_hall_capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id", "show_time", "movie_title",
            "cinema_hall_name", "cinema_hall_capacity"
        )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)
