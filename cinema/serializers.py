from rest_framework import serializers

from cinema.models import (
	Genre,
	Actor,
	CinemaHall,
	Movie,
	MovieSession
)


class GenreSerializer(serializers.ModelSerializer):
	class Meta:
		model = Genre
		fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Actor
		fields = ("id", "first_name", "last_name", "full_name")


class CinemaHallSerializer(serializers.ModelSerializer):
	class Meta:
		model = CinemaHall
		fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieListSerializer(MovieSerializer):
	genres = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='name'
	)
	actors = serializers.SlugRelatedField(
		many=True,
		read_only=True,
		slug_field='full_name'
	)

	class Meta:
		model = Movie
		fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieDetailSerializer(MovieSerializer):
	genres = GenreSerializer(many=True, read_only=True)
	actors = ActorSerializer(many=True, read_only=True)

	class Meta:
		model = Movie
		fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = MovieSession
		fields = "__all__"
