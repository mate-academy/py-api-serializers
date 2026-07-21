from rest_framework import serializers

from cinema.models import (Movie,
                           Genre,
                           Actor,
                           CinemaHall,
                           MovieSession)


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = (
            "id",
            "first_name",
            "last_name",
            "full_name"
        )

    def create(self, validated_data: dict) -> Actor:
        return Actor.objects.create(**validated_data)

    def update(self, instance: Actor, validated_data: dict) -> Actor:
        instance.first_name = validated_data.get(
            "first_name",
            instance.first_name)
        instance.last_name = validated_data.get(
            "last_name",
            instance.last_name)
        instance.save()
        return instance

    def get_full_name(self, obj: Actor) -> str:
        return str(obj)


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = "__all__"

    def create(self, validated_data: dict) -> Genre:
        return Genre.objects.create(**validated_data)

    def update(self,
               instance: Genre,
               validated_data: dict) -> Genre:
        instance.name = validated_data.get(
            "name",
            instance.name)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieListSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    genres = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors")

    def get_genres(self, obj: Movie) -> list[str]:
        return [f"{genres.name}" for genres in obj.genres.all()]

    def get_actors(self, obj: Movie) -> list[str]:
        return [f"{actor.first_name} {actor.last_name}"
                for actor in obj.actors.all()]


class MovieRetrieveSerializer(MovieListSerializer):
    actors = ActorSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "duration",
            "genres",
            "actors")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = "__all__"

    def create(self, validated_data: dict) -> CinemaHall:
        return CinemaHall.objects.create(**validated_data)

    def update(self,
               instance: CinemaHall,
               validated_data: dict) -> CinemaHall:
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get(
            "seats_in_row", instance.seats_in_row
        )
        instance.save()
        return instance


class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = "__all__"

    def create(self, validated_data: dict) -> MovieSession:
        return MovieSession.objects.create(**validated_data)

    def update(self,
               instance: MovieSession,
               validated_data: dict) -> MovieSession:
        instance.show_time = validated_data.get(
            "show_time",
            instance.show_time)
        instance.save()
        return instance


class MovieSessionListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    cinema_hall_name = serializers.SerializerMethodField()
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

    def get_movie_title(self, obj: MovieSession) -> str:
        return obj.movie.title

    def get_cinema_hall_name(self, obj: MovieSession) -> str:
        return obj.cinema_hall.name

    def get_cinema_hall_capacity(self, obj: MovieSession) -> int:
        return obj.cinema_hall.capacity


class CinemaHallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = (
            "id",
            "name",
            "rows",
            "seats_in_row",
            "capacity")


class MovieSessionRetrieveSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(many=False, read_only=True)
    cinema_hall = CinemaHallListSerializer(many=False, read_only=True)

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie",
            "cinema_hall")
