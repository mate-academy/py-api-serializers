from rest_framework import serializers

from cinema.models import Genre, Actor, CinemaHall, Movie, MovieSession, Order, Ticket


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only = ("id",)


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")
        read_only = ("id",)


class ActorListingField(serializers.RelatedField):
    def to_representation(self, value):
        full_name = value.first_name + " " + value.last_name
        return {
            "id": value.id,
            "first_name": value.first_name,
            "last_name": value.last_name,
            "full_name": full_name
        }


class ActorListSerializer(ActorSerializer):
    full_name = ActorListingField(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")

    # def get_full_name(self, obj):
    #     return str(obj)


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]
        read_only = ("id",)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "description", "duration", "genres", "actors"]
        read_only = ("id",)


# class ActorListingField(serializers.RelatedField):
#     def to_representation(self, value):
#         full_name = value.first_name + " " + value.last_name
#         return {
#             "id": value.id,
#             "first_name": value.first_name,
#             "last_name": value.last_name,
#             "full_name": full_name
#         }


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorListSerializer(many=True, read_only=True)


class MovieListSerializer(MovieSerializer):
    genres = serializers.StringRelatedField(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ["id", "movie", "cinema_hall", "show_time"]
        read_only = ("id",)


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(source="cinema_hall.capacity")

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity")


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(read_only=True)
    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "created_at", "user"]
        read_only = ("id",)


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["id", "movie_session", "order", "row", "seat"]
