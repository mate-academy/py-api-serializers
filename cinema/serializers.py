from rest_framework import serializers
from .models import Genre, Actor, CinemaHall, Movie, MovieSession


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Actor
        fields = "__all__"

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class CinemaHallSerializer(serializers.ModelSerializer):
    capacity = serializers.SerializerMethodField()

    class Meta:
        model = CinemaHall
        fields = ["id", "name", "rows", "seats_in_row", "capacity"]

    def get_capacity(self, obj):
        return obj.capacity


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        actors = representation["actors"]
        representation["actors"] = [actor["full_name"] for actor in actors]

        genres = representation["genres"]
        representation["genres"] = [genre["name"] for genre in genres]

        return representation


class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, required=False)
    actors = ActorSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = "__all__"

    def create(self, validated_data):
        genres_data = validated_data.pop("genres", [])
        actors_data = validated_data.pop("actors", [])

        movie = Movie.objects.create(**validated_data)

        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            movie.genres.add(genre)

        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)

        return movie

    def update(self, instance, validated_data):
        genres_data = validated_data.pop("genres", [])
        actors_data = validated_data.pop("actors", [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.genres.clear()
        instance.actors.clear()

        for genre_data in genres_data:
            genre, _ = Genre.objects.get_or_create(**genre_data)
            instance.genres.add(genre)

        for actor_data in actors_data:
            actor, _ = Actor.objects.get_or_create(**actor_data)
            instance.actors.add(actor)

        instance.save()
        return instance


class MovieSessionListSerializer(serializers.ModelSerializer):
    show_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name", read_only=True
    )
    cinema_hall_capacity = serializers.IntegerField(
        source="cinema_hall.capacity", read_only=True
    )

    class Meta:
        model = MovieSession
        fields = (
            "id",
            "show_time",
            "movie_title",
            "cinema_hall_name",
            "cinema_hall_capacity",
        )


class MovieSessionDetailSerializer(serializers.ModelSerializer):
    show_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    movie = MovieDetailSerializer()
    cinema_hall = CinemaHallSerializer()

    class Meta:
        model = MovieSession
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        actors = representation["movie"]["actors"]
        representation["movie"]["actors"] = [
            actor["full_name"] for actor in actors
        ]

        genres = representation["movie"]["genres"]
        representation["movie"]["genres"] = [genre["name"] for genre in genres]

        return representation
