from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from cinema.models import Actor
from cinema.serializers import ActorSerializer
from rest_framework.test import APITestCase


ACTOR_URL = reverse('actor-list')

def detail_url(actor_id) -> object:
    return reverse('actor-detail', args=[actor_id])


class ActorApiTests(APITestCase):
    def test_get_actors(self) -> None:
        Actor.objects.create(first_name='Tom', last_name='Hanks')
        Actor.objects.create(first_name='Keanu', last_name='Reeves')
        response = self.client.get(ACTOR_URL)

        actors = Actor.objects.all().order_by('id')
        serializer = ActorSerializer(actors, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_post_actors(self) -> None:
        payload = {'first_name': 'Tom', 'last_name': 'Hanks'}
        response = self.client.post(ACTOR_URL, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Actor.objects.count(), 1)
        self.assertEqual(Actor.objects.get().first_name, 'Tom')
        self.assertEqual(Actor.objects.get().last_name, 'Hanks')

    def test_get_actor(self) -> None:
        actor = Actor.objects.create(first_name='Tom', last_name='Hanks')
        url = detail_url(actor.id)
        response = self.client.get(url)

        serializer = ActorSerializer(actor)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_put_actor(self) -> None:
        actor = Actor.objects.create(first_name='Tom', last_name='Hanks')
        payload = {'first_name': 'Tom', 'last_name': 'Cruise'}
        url = detail_url(actor.id)
        response = self.client.put(url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, 'Tom')
        self.assertEqual(actor.last_name, 'Cruise')

    def test_delete_actor(self) -> None:
        actor = Actor.objects.create(first_name='Tom', last_name='Hanks')
        url = detail_url(actor.id)
        self.client.delete(url)
        db_actors_id_1 = Actor.objects.filter(id=actor.id)
        self.assertEqual(db_actors_id_1.count(), 0)
