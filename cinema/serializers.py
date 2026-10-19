from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession, Order, Ticket


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Actor
        fields = ["id", "first_name", "last_name", "full_name"]

    def get_full_name(self, obj: Actor) -> str:
        return f"{obj.first_name} {obj.last_name}"

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.IntegerField(read_only=True)
    class Meta:
        model = CinemaHall
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"



class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()

    actors_data = serializers.ListField(
        child=serializers.DictField(),
        write_only=True,
        required=False,
    )

    actor_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
        write_only=True,
        source="actors",
        required=False,
    )

    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        write_only=True,
        source="genres",
        required=False,
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors",
            "actor_ids",
            "genre_ids",
            "actors_data",
        ]

    def get_genres(self, obj: Movie) -> list[str]:
        return list(obj.genres.values_list("name", flat=True))

    def get_actors(self, obj: Movie) -> list[str]:
        return [
            f"{actor.first_name} {actor.last_name}"
            for actor in obj.actors.all()
        ]


class MovieCreateSerializer(serializers.ModelSerializer):
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
        required=False,
    )
    genres = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        many=True,
        required=False,
    )

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "description",
            "duration",
            "actors",
            "genres",
        ]

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(source="cinema_hall.name", read_only=True)
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity", read_only=True)

    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity"]


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = [
            "id",
            "show_time",
            "movie",
            "cinema_hall",
        ]


class MovieSessionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "show_time", "movie", "cinema_hall"]
