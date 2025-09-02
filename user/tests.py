from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class UserApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            email="testuser@example.com",
        )

    def test_user_list(self):
        response = self.client.get("/api/user/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(
            any(
                u["username"] == "testuser"
                for u in response.json()
            )
        )

    def test_user_detail(self):
        response = self.client.get(f"/api/user/users/{self.user.pk}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["username"], "testuser")

    def test_create_user(self):
        payload = {
            "username": "newuser",
            "password": "newpass123",
            "email": "newuser@example.com",
        }
        response = self.client.post("/api/user/users/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="newuser").exists())
