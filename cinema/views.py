from rest_framework.viewsets import ModelViewSet

from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
