from rest_framework.viewsets import ModelViewSet

from cinema.models import (
    Genre
)
from cinema.serializers import (
    GenreSerializer
)


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
