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
	pass


class CinemaHallSerializer(serializers.ModelSerializer):
	pass


class MovieSerializer(serializers.ModelSerializer):
	pass


class MovieSessionSerializer(serializers.ModelSerializer):
	pass