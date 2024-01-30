from rest_framework import generics, viewsets

from cinema.models import Genre

from cinema.serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

