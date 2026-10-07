from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from rest_framework import status
from rest_framework.test import APIClient

from cinema.models import Actor, CinemaHall, Genre, Movie, MovieSession


class ApiContractTests(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.genre = Genre.objects.create(name="Drama")
        self.other_genre = Genre.objects.create(name="Comedy")
        self.actor = Actor.objects.create(
            first_name="Kate", last_name="Winslet"
        )
        self.other_actor = Actor.objects.create(
            first_name="Daniel", last_name="Radcliffe"
        )
        self.hall = CinemaHall.objects.create(
            name="Blue", rows=10, seats_in_row=14
        )
        self.other_hall = CinemaHall.objects.create(
            name="Green", rows=6, seats_in_row=8
        )
        self.movie = Movie.objects.create(
            title="Zeta Movie",
            description="First movie description",
            duration=120,
        )
        self.movie.genres.add(self.genre, self.other_genre)
        self.movie.actors.add(self.actor, self.other_actor)
        self.other_movie = Movie.objects.create(
            title="Alpha Movie",
            description="Second movie description",
            duration=90,
        )
        self.other_movie.genres.add(self.other_genre)
        self.other_movie.actors.add(self.other_actor)
        self.show_time = timezone.now().replace(microsecond=0)
        self.session = MovieSession.objects.create(
            movie=self.movie,
            cinema_hall=self.hall,
            show_time=self.show_time,
        )

    def test_movie_writes_create_replace_and_update_relations(self) -> None:
        payload = {
            "title": "New Movie",
            "description": "New movie description",
            "duration": 100,
            "genres": [self.genre.pk],
            "actors": [self.actor.pk],
        }
        response = self.client.post(
            "/api/cinema/movies/", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        movie = Movie.objects.get(pk=response.data["id"])
        self.assertEqual(movie.title, payload["title"])
        self.assertEqual(movie.description, payload["description"])
        self.assertEqual(movie.duration, payload["duration"])
        self.assertQuerysetEqual(
            movie.genres.values_list("pk", flat=True), [self.genre.pk]
        )
        self.assertQuerysetEqual(
            movie.actors.values_list("pk", flat=True), [self.actor.pk]
        )

        updated_payload = {
            **payload,
            "title": "Updated Movie",
            "description": "Updated movie description",
            "duration": 140,
            "genres": [self.other_genre.pk],
            "actors": [self.other_actor.pk],
        }
        detail_url = f"/api/cinema/movies/{movie.pk}/"
        response = self.client.put(
            detail_url, updated_payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertEqual(movie.title, updated_payload["title"])
        self.assertEqual(movie.description, updated_payload["description"])
        self.assertEqual(movie.duration, updated_payload["duration"])
        self.assertQuerysetEqual(
            movie.genres.values_list("pk", flat=True), [self.other_genre.pk]
        )
        self.assertQuerysetEqual(
            movie.actors.values_list("pk", flat=True), [self.other_actor.pk]
        )

        response = self.client.patch(
            detail_url, {"genres": [], "actors": []}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("genres", response.data)
        self.assertIn("actors", response.data)
        movie.refresh_from_db()
        self.assertQuerysetEqual(
            movie.genres.values_list("pk", flat=True), [self.other_genre.pk]
        )
        self.assertQuerysetEqual(
            movie.actors.values_list("pk", flat=True), [self.other_actor.pk]
        )
        self.assertEqual(movie.title, updated_payload["title"])
        self.assertEqual(movie.description, updated_payload["description"])
        self.assertEqual(movie.duration, updated_payload["duration"])

        response = self.client.patch(
            detail_url, {"genres": [self.genre.pk]}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertQuerysetEqual(
            movie.genres.values_list("pk", flat=True), [self.genre.pk]
        )
        self.assertQuerysetEqual(
            movie.actors.values_list("pk", flat=True), [self.other_actor.pk]
        )
        self.assertEqual(movie.title, updated_payload["title"])
        self.assertEqual(movie.description, updated_payload["description"])
        self.assertEqual(movie.duration, updated_payload["duration"])

    def test_movie_rejects_invalid_relation_ids_and_nested_objects(
        self,
    ) -> None:
        payload = {
            "title": "Invalid Relations Movie",
            "description": "Otherwise valid movie",
            "duration": 100,
            "genres": [self.genre.pk],
            "actors": [self.actor.pk],
        }
        movie_count = Movie.objects.count()
        relations = (
            ("genres", self.genre, self.other_genre),
            ("actors", self.actor, self.other_actor),
        )
        for field, relation, other_relation in relations:
            missing_pk = max(relation.pk, other_relation.pk) + 1
            for invalid_value in ([missing_pk], [{"id": relation.pk}]):
                with self.subTest(field=field, value=invalid_value):
                    response = self.client.post(
                        "/api/cinema/movies/",
                        {**payload, field: invalid_value},
                        format="json",
                    )
                    self.assertEqual(
                        response.status_code, status.HTTP_400_BAD_REQUEST
                    )
                    self.assertIn(field, response.data)
                    self.assertEqual(Movie.objects.count(), movie_count)

    def test_read_serializers_return_expected_movie_session_and_hall_shapes(
        self,
    ) -> None:
        response = self.client.get("/api/cinema/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movies_by_id = {item["id"]: item for item in response.data}
        movie_data = movies_by_id[self.movie.pk]
        expected_movie = {
            "id": self.movie.pk,
            "title": self.movie.title,
            "description": self.movie.description,
            "duration": self.movie.duration,
            "genres": ["Drama", "Comedy"],
            "actors": ["Kate Winslet", "Daniel Radcliffe"],
        }
        self.assertEqual(set(movie_data), set(expected_movie))
        for field in ("id", "title", "description", "duration"):
            self.assertEqual(movie_data[field], expected_movie[field])
        self.assertCountEqual(movie_data["genres"], expected_movie["genres"])
        self.assertCountEqual(movie_data["actors"], expected_movie["actors"])

        response = self.client.get(f"/api/cinema/movies/{self.movie.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(set(response.data), set(expected_movie))
        for field in ("id", "title", "description", "duration"):
            self.assertEqual(response.data[field], expected_movie[field])
        self.assertCountEqual(
            response.data["genres"],
            [
                {"id": self.genre.pk, "name": "Drama"},
                {"id": self.other_genre.pk, "name": "Comedy"},
            ],
        )
        self.assertCountEqual(
            response.data["actors"],
            [
                {
                    "id": self.actor.pk,
                    "first_name": "Kate",
                    "last_name": "Winslet",
                    "full_name": "Kate Winslet",
                },
                {
                    "id": self.other_actor.pk,
                    "first_name": "Daniel",
                    "last_name": "Radcliffe",
                    "full_name": "Daniel Radcliffe",
                },
            ],
        )

        response = self.client.get("/api/cinema/movie_sessions/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sessions_by_id = {item["id"]: item for item in response.data}
        session_data = sessions_by_id[self.session.pk]
        self.assertEqual(
            set(session_data),
            {
                "id",
                "show_time",
                "movie_title",
                "cinema_hall_name",
                "cinema_hall_capacity",
            },
        )
        self.assertEqual(session_data["movie_title"], self.movie.title)
        self.assertEqual(session_data["cinema_hall_name"], self.hall.name)
        self.assertEqual(session_data["cinema_hall_capacity"], 140)
        parsed_show_time = parse_datetime(session_data["show_time"])
        self.assertIsNotNone(parsed_show_time)
        self.assertTrue(timezone.is_aware(parsed_show_time))
        self.assertEqual(parsed_show_time, self.session.show_time)

        response = self.client.get(
            f"/api/cinema/movie_sessions/{self.session.pk}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            set(response.data), {"id", "show_time", "movie", "cinema_hall"}
        )
        self.assertEqual(response.data["id"], self.session.pk)
        parsed_show_time = parse_datetime(response.data["show_time"])
        self.assertIsNotNone(parsed_show_time)
        self.assertTrue(timezone.is_aware(parsed_show_time))
        self.assertEqual(parsed_show_time, self.session.show_time)
        self.assertEqual(set(response.data["movie"]), set(expected_movie))
        for field in ("id", "title", "description", "duration"):
            self.assertEqual(
                response.data["movie"][field], expected_movie[field]
            )
        for field in ("genres", "actors"):
            self.assertCountEqual(
                response.data["movie"][field], expected_movie[field]
            )
        self.assertEqual(
            response.data["cinema_hall"],
            {
                "id": self.hall.pk,
                "name": "Blue",
                "rows": 10,
                "seats_in_row": 14,
                "capacity": 140,
            },
        )

        response = self.client.get("/api/cinema/cinema_halls/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        halls_by_id = {item["id"]: item for item in response.data}
        for hall in (self.hall, self.other_hall):
            self.assertEqual(
                halls_by_id[hall.pk],
                {
                    "id": hall.pk,
                    "name": hall.name,
                    "rows": hall.rows,
                    "seats_in_row": hall.seats_in_row,
                    "capacity": hall.rows * hall.seats_in_row,
                },
            )

    def test_session_create_update_patch_and_delete(self) -> None:
        payload = {
            "movie": self.movie.pk,
            "cinema_hall": self.hall.pk,
            "show_time": self.show_time.isoformat(),
        }
        session_count = MovieSession.objects.count()
        response = self.client.post(
            "/api/cinema/movie_sessions/", payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MovieSession.objects.count(), session_count + 1)
        self.assertIn("id", response.data)
        self.assertNotEqual(response.data["id"], self.session.pk)
        session = MovieSession.objects.get(pk=response.data["id"])
        self.assertEqual(session.movie_id, self.movie.pk)
        self.assertEqual(session.cinema_hall_id, self.hall.pk)
        self.assertEqual(session.show_time, self.show_time)

        updated_time = self.show_time + timedelta(hours=1)
        detail_url = f"/api/cinema/movie_sessions/{session.pk}/"
        response = self.client.put(
            detail_url,
            {
                "movie": self.other_movie.pk,
                "cinema_hall": self.other_hall.pk,
                "show_time": updated_time.isoformat(),
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        session.refresh_from_db()
        self.assertEqual(session.movie_id, self.other_movie.pk)
        self.assertEqual(session.cinema_hall_id, self.other_hall.pk)
        self.assertEqual(session.show_time, updated_time)

        response = self.client.patch(
            detail_url, {"movie": self.movie.pk}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        session.refresh_from_db()
        self.assertEqual(session.movie_id, self.movie.pk)
        self.assertEqual(session.cinema_hall_id, self.other_hall.pk)
        self.assertEqual(session.show_time, updated_time)

        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(MovieSession.objects.filter(pk=session.pk).exists())
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.delete(detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_session_rejects_missing_foreign_keys(self) -> None:
        payload = {
            "movie": self.movie.pk,
            "cinema_hall": self.hall.pk,
            "show_time": self.show_time.isoformat(),
        }
        session_count = MovieSession.objects.count()
        missing_ids = {
            "movie": max(self.movie.pk, self.other_movie.pk) + 1,
            "cinema_hall": max(self.hall.pk, self.other_hall.pk) + 1,
        }
        for field, missing_pk in missing_ids.items():
            with self.subTest(field=field):
                response = self.client.post(
                    "/api/cinema/movie_sessions/",
                    {**payload, field: missing_pk},
                    format="json",
                )
                self.assertEqual(
                    response.status_code, status.HTTP_400_BAD_REQUEST
                )
                self.assertIn(field, response.data)
                self.assertEqual(MovieSession.objects.count(), session_count)

    def test_actor_and_genre_detail_return_full_schema(self) -> None:
        response = self.client.get(f"/api/cinema/actors/{self.actor.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                "id": self.actor.pk,
                "first_name": "Kate",
                "last_name": "Winslet",
                "full_name": "Kate Winslet",
            },
        )
        response = self.client.get(f"/api/cinema/genres/{self.genre.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"id": self.genre.pk, "name": "Drama"})
