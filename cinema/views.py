from rest_framework import viewsets

from cinema.models import (
	Genre,
	Actor,
	CinemaHall,
	Movie,
	MovieSession
)
from cinema.serializers import (
	GenreSerializer,
	ActorSerializer,
	CinemaHallSerializer,
	MovieSerializer,
	MovieSessionSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
	queryset = Genre.objects.all()
	serializer_class = GenreSerializer
