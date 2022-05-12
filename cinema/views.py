from rest_framework import viewsets

from cinema.models import Genre
from cinema.serializers import GenreSerializers


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


