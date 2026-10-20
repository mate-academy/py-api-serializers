from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class SerializerContractTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.genre = Genre.objects.create(name="Drama")
        self.actor = Actor.objects.create(first_name="Kate", last_name="Winslet")
        self.movie = Movie.objects.create(
            title="Titanic", description="A movie", duration=123
        )
        self.movie.genres.add(self.genre)
        self.movie.actors.add(self.actor)
        self.hall = CinemaHall.objects.create(
            name="Blue", rows=10, seats_in_row=15
        )
        self.session = MovieSession.objects.create(
            movie=self.movie, cinema_hall=self.hall, show_time=timezone.now()
        )
        self.session_url = (
            f"/api/cinema/movie_sessions/{self.session.pk}/"
        )

    def test_computed_fields_ignore_input(self) -> None:
        response = self.client.patch(
            f"/api/cinema/actors/{self.actor.pk}/",
            {"first_name": "Emma", "full_name": "Forged"},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "Emma Winslet")
        response = self.client.patch(
            f"/api/cinema/cinema_halls/{self.hall.pk}/",
            {"rows": 20, "capacity": 1},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["capacity"], 300)

    def test_movie_relationships_can_be_replaced(self) -> None:
        genre = Genre.objects.create(name="Comedy")
        actor = Actor.objects.create(first_name="Emma", last_name="Watson")
        response = self.client.patch(
            f"/api/cinema/movies/{self.movie.pk}/",
            {"genres": [genre.pk], "actors": [actor.pk]},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(self.movie.genres.all()), [genre])
        self.assertEqual(list(self.movie.actors.all()), [actor])

    def test_session_put_and_patch_accept_relationship_ids(self) -> None:
        hall = CinemaHall.objects.create(name="VIP", rows=2, seats_in_row=5)
        response = self.client.put(
            self.session_url,
            {
                "movie": self.movie.pk,
                "cinema_hall": hall.pk,
                "show_time": "2026-11-01T12:00:00Z",
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.patch(
            self.session_url, {"cinema_hall": self.hall.pk}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.session.refresh_from_db()
        self.assertEqual(self.session.cinema_hall, self.hall)

    def test_session_invalid_relationship_is_rejected(self) -> None:
        response = self.client.patch(
            self.session_url, {"movie": self.movie.pk + 100}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.session.refresh_from_db()
        self.assertEqual(self.session.movie, self.movie)

    def test_session_delete_and_missing_detail(self) -> None:
        response = self.client.delete(self.session_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MovieSession.objects.exists())
        response = self.client.get(self.session_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_related_reads_have_bounded_query_counts(self) -> None:
        for index in range(3):
            movie = Movie.objects.create(
                title=f"Movie {index}", description="A movie", duration=90
            )
            movie.genres.add(self.genre)
            movie.actors.add(self.actor)
            MovieSession.objects.create(
                movie=movie, cinema_hall=self.hall, show_time=timezone.now()
            )
        with self.assertNumQueries(3):
            response = self.client.get("/api/cinema/movies/")
            self.assertEqual(len(response.data), 4)
        with self.assertNumQueries(1):
            response = self.client.get("/api/cinema/movie_sessions/")
            self.assertEqual(len(response.data), 4)
        with self.assertNumQueries(3):
            response = self.client.get(self.session_url)
            self.assertEqual(response.data["movie"]["actors"], ["Kate Winslet"])
