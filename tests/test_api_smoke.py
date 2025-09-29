import pytest
from datetime import timedelta
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from cinema.models import Genre, Actor, Movie, CinemaHall, MovieSession

@pytest.mark.django_db
def test_movies_list_and_detail_shapes() -> None:
    g = Genre.objects.create(name="Drama")
    a = Actor.objects.create(first_name="Tom", last_name="Hanks")
    m = Movie.objects.create(title="Forrest", description="desc", duration=120)
    m.genres.add(g)
    m.actors.add(a)

    client = APIClient()

    url_list = reverse("cinema:movie-list")
    r_list = client.get(url_list)
    assert r_list.status_code == 200
    data_list = r_list.json()
    assert isinstance(data_list, list)
    assert data_list, "Lista de filmes vazia"
    assert {"id", "title", "description", "duration", "genres", "actors"} <= set(data_list[0].keys())
    assert isinstance(data_list[0]["genres"], list)
    assert isinstance(data_list[0]["actors"], list)

    url_detail = reverse("cinema:movie-detail", args=[m.id])
    r_detail = client.get(url_detail)
    assert r_detail.status_code == 200
    data_detail = r_detail.json()
    # detail usa nested serializers
    assert isinstance(data_detail["genres"], list) and isinstance(data_detail["genres"][0], dict)
    assert isinstance(data_detail["actors"], list) and isinstance(data_detail["actors"][0], dict)

@pytest.mark.django_db
def test_movie_sessions_list_and_detail_shapes() -> None:
    g = Genre.objects.create(name="Action")
    a = Actor.objects.create(first_name="Keanu", last_name="Reeves")
    m = Movie.objects.create(title="Matrix", description="Neo", duration=136)
    m.genres.add(g)
    m.actors.add(a)
    hall = CinemaHall.objects.create(name="Hall 1", rows=10, seats_in_row=20)

    show_time = timezone.now() + timedelta(days=1)
    ms = MovieSession.objects.create(show_time=show_time, movie=m, cinema_hall=hall)

    client = APIClient()

    url_list = reverse("cinema:moviesession-list")
    r_list = client.get(url_list)
    assert r_list.status_code == 200
    data_list = r_list.json()
    assert isinstance(data_list, list)
    assert data_list, "Lista de sessões vazia"
    assert {"id", "show_time", "movie_title", "cinema_hall_name", "cinema_hall_capacity"} <= set(
        data_list[0].keys()
    )

    url_detail = reverse("cinema:moviesession-detail", args=[ms.id])
    r_detail = client.get(url_detail)
    assert r_detail.status_code == 200
    data_detail = r_detail.json()
    assert {"id", "show_time", "movie", "cinema_hall"} <= set(data_detail.keys())
    assert isinstance(data_detail["movie"], dict)
    assert isinstance(data_detail["cinema_hall"], dict)
