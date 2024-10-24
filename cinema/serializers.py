# write serializers here
from rest_framework import serializers

from cinema.models import Genre, CinemaHall, Actor, Movie, MovieSession, Order, Ticket


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = [
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity",
        ]


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


# class ActorListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fi
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_actors(self, obj):
        return [str(actor) for actor in obj.actors.all()]

    def get_genres(self, obj):
        return [str(genre) for genre in obj.genres.all()]


class MovieRetrieveSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"


class MovieLSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]

    def get_actors(self, obj):
        return [str(actor) for actor in obj.actors.all()]

    def get_genres(self, obj):
        return [str(genre) for genre in obj.genres.all()]


class MovieListSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        ]


class MovieRetrieveSessionSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
