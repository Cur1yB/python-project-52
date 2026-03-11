from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse_lazy as reverse

from statuses.models import Status
from tasks.models import Task
from users.models import User


class TestStatus(TestCase):
    fixtures = ["statuses.json", "users.json"]

    def setUp(self):
        self.user = User.objects.order_by("pk").first()
        if self.user is None:
            raise AssertionError("users.json не загрузился (нет пользователей).")
        self.status_obj = Status.objects.get(pk=1)

        self.status_data = {"name": "статус_обновлён"}

    def test_status_index_page(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses:index"))
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        test_status_data = {"name": "status_test"}
        status_count = Status.objects.count()

        self.client.force_login(user=self.user)
        response = self.client.post(reverse("statuses:create"), test_status_data)

        self.assertRedirects(response, reverse("statuses:index"))
        test_status = Status.objects.latest("id")
        self.assertEqual(test_status.name, test_status_data["name"])
        self.assertEqual(Status.objects.count(), status_count + 1)

    def test_read_status(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse("statuses:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.status_obj.name)

    def test_update_status(self):
        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("statuses:update", kwargs={"pk": self.status_obj.id}),
            self.status_data,
        )
        self.assertRedirects(response, reverse("statuses:index"))

        self.status_obj.refresh_from_db()
        self.assertEqual(self.status_obj.name, self.status_data["name"])

    def test_delete_status(self):
        test_status = Status.objects.create(name="status_test_2")
        status_count = Status.objects.count()

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse("statuses:delete", kwargs={"pk": test_status.id})
        )
        self.assertRedirects(response, reverse("statuses:index"))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Статус успешно удален")

        self.assertEqual(Status.objects.count(), status_count - 1)


    def test_delete_task_status(self):
        status_count = Status.objects.count()
        self.client.force_login(user=self.user)

        Task.objects.create(
            name="test",
            author=self.user,
            status=self.status_obj,
        )

        response = self.client.post(
            reverse("statuses:delete", kwargs={"pk": self.status_obj.id})
        )

        self.assertRedirects(response, reverse("statuses:index"))
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Невозможно удалить статус, потому что он используется",
        )
        self.assertEqual(Status.objects.count(), status_count)