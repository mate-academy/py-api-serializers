from rest_framework.viewsets import ModelViewSet
from cinema.models import MovieSession
from cinema.serializers.movie_session import (
    MovieSessionListSerializer,
    MovieSessionDetailSerializer
)


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
