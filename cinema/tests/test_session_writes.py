"""Regression tests for session writes and serializer selection."""
from __future__ import annotations

from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from cinema.models import CinemaHall, Movie, MovieSession


class SessionWriteTests(APITestCase):
    """Cover session operations missing from the starter tests."""

    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title="Arrival", description="First contact.", duration=116
        )
        self.hall = CinemaHall.objects.create(
            name="Blue", rows=10, seats_in_row=12
        )
        self.session = MovieSession.objects.create(
            movie=self.movie,
            cinema_hall=self.hall,
            show_time=timezone.now(),
        )
        self.url = f"/api/cinema/movie_sessions/{self.session.pk}/"

    def test_put_changes_relations_using_ids(self) -> None:
        """Writable serializers must not ignore related-object IDs."""
        other_hall = CinemaHall.objects.create(
            name="Green", rows=5, seats_in_row=8
        )
        response = self.client.put(
            self.url,
            {
                "movie": self.movie.pk,
                "cinema_hall": other_hall.pk,
                "show_time": timezone.now().isoformat(),
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.session.refresh_from_db()
        self.assertEqual(self.session.cinema_hall_id, other_hall.pk)

    def test_invalid_relation_does_not_change_session(self) -> None:
        response = self.client.patch(
            self.url, {"movie": 99999}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.session.refresh_from_db()
        self.assertEqual(self.session.movie_id, self.movie.pk)

    def test_delete_and_missing_detail(self) -> None:
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            MovieSession.objects.filter(pk=self.session.pk).exists()
        )
        self.assertEqual(
            self.client.get(self.url).status_code,
            status.HTTP_404_NOT_FOUND,
        )

    def test_list_has_exact_summary_fields(self) -> None:
        response = self.client.get("/api/cinema/movie_sessions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data[0]),
            {
                "id", "show_time", "movie_title",
                "cinema_hall_name", "cinema_hall_capacity",
            },
        )
        self.assertEqual(response.data[0]["cinema_hall_capacity"], 120)
