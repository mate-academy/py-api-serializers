from rest_framework.viewsets import ModelViewSet
from cinema.models import Actor
from cinema.serializers.actor import ActorSerializer


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
