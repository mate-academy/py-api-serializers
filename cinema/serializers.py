from rest_framework import serializers

from cinema.models import Movie, Genre, Actor, MovieSession, CinemaHall


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class GenreSerializer(serializers.ModelSerializer):
    def to_representation(self, value):
        if self.context.get("view").action == "list":
            return value.name
        return super().to_representation(value)

    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def to_representation(self, value):
        if self.context.get("view").action == "list":
            return f"{value.first_name} {value.last_name}"
        return super().to_representation(value)

    def get_full_name(self, instance):
        return f"{instance.first_name} {instance.last_name}"

    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name", "full_name")


class MovieListSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    def get_actors(self, instance):
        return [f"{actor.first_name} {actor.last_name}" for actor in
                instance.actors.all()]


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)


class MovieSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")


class MovieSessionListSerializer(MovieSessionSerializer):
    movie_title = serializers.CharField(source="movie.title")
    cinema_hall_name = serializers.CharField(source="cinema_hall.name")
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity"
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity"
        )


class CinemaHallSerializer(serializers.ModelSerializer):

    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row")


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")
