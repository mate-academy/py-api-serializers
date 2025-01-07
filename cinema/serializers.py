# write serializers here
from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    full_name = serializers.SerializerMethodField("get_full_name")

    class Meta:
        model = Actor
        fields = "id", "first_name", "last_name", "full_name"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)

    class Meta:
        model = CinemaHall
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(MovieSerializer):
    actors = serializers.StringRelatedField(many=True, read_only=True)
    genres = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="name"
    )


class MovieRetrieveSerializer(MovieSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieSessionListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    show_time = serializers.CharField(read_only=True)
    movie_title = serializers.CharField(
        source="movie.title", read_only=True
    )
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )


class MovieSessionRetrieveSerializer(MovieSessionSerializer):
    movie = MovieListSerializer()
    cinema_hall = CinemaHallSerializer()
