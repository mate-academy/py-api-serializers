from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre, Actor
)
from cinema.serializers import (
    GenreSerializer, ActorSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
