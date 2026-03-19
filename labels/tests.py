from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse_lazy

from labels.models import Label
from statuses.models import Status
from tasks.models import Task
from users.models import User


class TestLabels(TestCase):
    fixtures = ["users.json", "statuses.json", "labels.json"]

    def setUp(self):
        self.user = User.objects.order_by("pk").first()
        if self.user is None:
            raise AssertionError("Не загрузилась фикстура users.json")

        self.status = Status.objects.order_by("pk").first()
        if self.status is None:
            raise AssertionError("Не загрузилась фикстура statuses.json")

        self.label_obj = Label.objects.order_by("pk").first()
        if self.label_obj is None:
            raise AssertionError("Не загрузилась фикстура labels.json")

    def test_labels_index_page_not_logged_in(self):
        response = self.client.get(reverse_lazy("labels:index"))
        self.assertRedirects(response, expected_url="/login/?next=/labels/")

    def test_labels_index_page_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy("labels:index"))
        self.assertEqual(response.status_code, 200)

    def test_create_label(self):
        test_label_data = {"name": "test_label"}
        total_labels = Label.objects.count()

        self.client.force_login(self.user)
        response = self.client.post(reverse_lazy("labels:create"), test_label_data)

        self.assertRedirects(response, expected_url=reverse_lazy("labels:index"))
        test_label = Label.objects.latest("id")
        self.assertEqual(test_label.name, test_label_data["name"])
        self.assertEqual(Label.objects.count(), total_labels + 1)

    def test_update_label(self):
        update_label = {"name": "new_name"}
        label_id = self.label_obj.id

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy("labels:update", kwargs={"pk": label_id}),
            update_label,
        )
        self.assertEqual(response.status_code, 302)

        updated_label = Label.objects.get(id=label_id)
        self.assertEqual(updated_label.name, update_label["name"])

    def test_delete_label(self):
        label = Label.objects.create(name="to_delete")
        total_labels = Label.objects.count()

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy("labels:delete", kwargs={"pk": label.id})
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Метка успешно удалена")

        self.assertEqual(Label.objects.count(), total_labels - 1)

    def test_delete_task_label(self):
        total_labels = Label.objects.count()

        task = Task.objects.create(
            name="test",
            author=self.user,
            status=self.status,
        )
        task.labels.add(self.label_obj)

        self.client.force_login(user=self.user)
        response = self.client.post(
            reverse_lazy("labels:delete", kwargs={"pk": self.label_obj.id})
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Невозможно удалить метку, потому что она используется",
        )

        self.assertRedirects(response, expected_url=reverse_lazy("labels:index"))
        self.assertEqual(Label.objects.count(), total_labels)
