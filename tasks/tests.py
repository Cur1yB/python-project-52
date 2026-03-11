from django.test import TestCase
from django.urls import reverse_lazy

from statuses.models import Status
from tasks.models import Task
from users.models import User


class TestTask(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.user = User.objects.order_by("pk").first()
        if self.user is None:
            raise AssertionError("Не загрузилась фикстура users.json")

        self.status = Status.objects.order_by("pk").first()
        if self.status is None:
            raise AssertionError("Не загрузилась фикстура statuses.json")

        self.task_obj = Task.objects.order_by("pk").first()
        if self.task_obj is None:
            raise AssertionError("Не загрузилась фикстура tasks.json")

    def test_task_page_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(reverse_lazy("tasks:index"))
        self.assertEqual(response.status_code, 200)

    def test_task_page_logout(self):
        response = self.client.get(reverse_lazy("tasks:index"))
        self.assertRedirects(response, "/login/?next=/tasks/")

    def test_create_task(self):
        test_task_data = {
            "name": "test_task",
            "description": "описание",
            "status": self.status.id,
            "executor": "",
            "labels": [],
        }
        tasks_count = Task.objects.count()

        self.client.force_login(user=self.user)
        response = self.client.post(reverse_lazy("tasks:create"), test_task_data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("tasks:index"))

        test_task = Task.objects.latest("id")
        self.assertEqual(test_task.name, test_task_data["name"])
        self.assertEqual(test_task.description, test_task_data["description"])
        self.assertEqual(test_task.status_id, self.status.id)
        self.assertEqual(test_task.author_id, self.user.id)
        self.assertEqual(Task.objects.count(), tasks_count + 1)

    def test_update_task(self):
        update_task = {
            "name": "new_name",
            "description": "новое описание",
            "status": self.status.id,
            "executor": "",
            "labels": [],
        }

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy("tasks:update", kwargs={"pk": self.task_obj.id}),
            update_task,
        )
        self.assertRedirects(response, reverse_lazy("tasks:index"))

        self.task_obj.refresh_from_db()
        self.assertEqual(self.task_obj.name, update_task["name"])
        self.assertEqual(self.task_obj.description, update_task["description"])
        self.assertEqual(self.task_obj.status_id, self.status.id)

    def test_delete_task(self):
        task = Task.objects.create(
            name="to_delete",
            description="описание",
            author=self.user,
            status=self.status,
        )
        tasks_count = Task.objects.count()

        self.client.force_login(user=self.user)
        response = self.client.post(reverse_lazy("tasks:delete", kwargs={"pk": task.id}))

        self.assertRedirects(response, reverse_lazy("tasks:index"))
        self.assertEqual(Task.objects.count(), tasks_count - 1)
