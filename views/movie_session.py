from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from cinema.models import MovieSession
from cinema.serializers.movie_session import (
    MovieSessionListSerializer,
    MovieSessionDetailSerializer
)


class MovieSessionViewSet(ModelViewSet):
    queryset = MovieSession.objects.select_related("movie", "cinema_hall")  # Optimized queryset

    def get_serializer_class(self) -> type[serializers.ModelSerializer]:
        if self.action == "list":
            return MovieSessionListSerializer
        return MovieSessionDetailSerializer
