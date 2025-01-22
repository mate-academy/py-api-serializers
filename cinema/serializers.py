from rest_framework import serializers

from cinema.models import Movie, Actor, Genre, CinemaHall, MovieSession


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name",
                                                 instance.first_name)
        instance.last_name = validated_data.get("last_name",
                                                instance.last_name)
        instance.save()
        return instance


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class CinemaHallSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    rows = serializers.IntegerField()
    seats_in_row = serializers.IntegerField()

    def create(self, validated_data):
        return CinemaHall.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.rows = validated_data.get("rows", instance.rows)
        instance.seats_in_row = validated_data.get("seats_in_row",
                                                   instance.seats_in_row)
        instance.save()
        return instance


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    actors = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Actor.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset=Genre.objects.all())

    def create(self, validated_data):
        actors = validated_data.pop("actors", [])
        genres = validated_data.pop("genres", [])
        movie = Movie.objects.create(**validated_data)
        movie.actors.set(actors)
        movie.genres.set(genres)
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description",
                                                  instance.description)
        instance.duration = validated_data.get("duration",
                                               instance.duration)
        if "actors" in validated_data:
            instance.actors.set(validated_data["actors"])
        if "genres" in validated_data:
            instance.genres.set(validated_data["genres"])
        instance.save()
        return instance


class MovieSessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    show_time = serializers.DateTimeField()
    movie = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all())
    cinema_hall = serializers.PrimaryKeyRelatedField(queryset=CinemaHall.objects.all())

    def create(self, validated_data):
        return MovieSession.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.show_time = validated_data.get("show_time", instance.show_time)
        if "movie" in validated_data:
            instance.movie.set(validated_data["movie"])
        if "cinema_hall" in validated_data:
            instance.cinema_hall.set(validated_data["cinema_hall"])
        instance.save()
        return instance