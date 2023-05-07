from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )


    class Meta:
        model = Movie
        fields = "__all__"


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Movie
        fields = "__all__"


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    cinema_hall_name = serializers.SerializerMethodField()
    cinema_hall_capacity = serializers.SerializerMethodField()

    def get_movie_title(self, obj):
        return obj.movie.title

    def get_cinema_hall_name(self, obj):
        return obj.cinema_hall.name

    def get_cinema_hall_capacity(self, obj):
        return obj.cinema_hall.capacity

    def create(self, validated_data):
        movie_data = validated_data.pop("movie")
        cinema_hall_data = validated_data.pop("cinema_hall")

        try:
            movie = Movie.objects.get(id=movie_data.id)
        except Movie.DoesNotExist:
            raise serializers.ValidationError("Invalid movie.")

        try:
            cinema_hall = CinemaHall.objects.get(id=cinema_hall_data.id)
        except CinemaHall.DoesNotExist:
            raise serializers.ValidationError("Invalid cinema hall.")

        movie_session = MovieSession.objects.create(
            movie=movie, cinema_hall=cinema_hall, **validated_data
        )

        return movie_session

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie",
            "movie_title",
            "cinema_hall",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]




class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = "__all__"
