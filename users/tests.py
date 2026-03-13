from django.test import TestCase
from django.urls import reverse_lazy as reverse

from .models import User


class TestUser(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user = User.objects.order_by("pk").first()
        self.user_data = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "username": self.user.username,
        }

    def test_users_page_status_200(self):
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        test_user_data = {
            "first_name": "test_name",
            "last_name": "testov",
            "username": "test_test",
            "password1": "test123@q",
            "password2": "test123@q",
        }
        total_users = User.objects.count()

        response = self.client.post(reverse("users:create"), test_user_data)
        self.assertRedirects(response, reverse("login"))

        test_user = User.objects.last()
        self.assertEqual(test_user.username, test_user_data["username"])
        self.assertEqual(User.objects.count(), total_users + 1)

    def test_read_user(self):
        response = self.client.get(reverse("users:users"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.username)
        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.last_name)

    def test_update_user(self):
        self.user.set_password("OldPass123@")
        self.user.save()

        update_user = {
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "username": "pupa",
            "password1": "NewPass123@",
            "password2": "NewPass123@",
        }

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("users:update", kwargs={"pk": self.user.id}),
            update_user,
        )
        self.assertRedirects(response, reverse("users:users"))

        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "pupa")

    def test_delete_user(self):
        user = User.objects.create_user(
            username="todelete",
            password="Pass123@"
        )
        total_users = User.objects.count()

        self.client.force_login(user=user)
        response = self.client.post(
            reverse(
                "users:delete",
                kwargs={"pk": user.id}
            )
        )

        self.assertRedirects(response, reverse("users:users"))
        self.assertEqual(User.objects.count(), total_users - 1)
