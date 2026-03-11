from django.db import models

from labels.models import Label
from statuses.models import Status
from users.models import User


class Task(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(max_length=255, blank=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="author",
        blank=False,
        null=False,
    )
    executor = models.ForeignKey(
        User, on_delete=models.PROTECT, blank=True, null=True
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False)
    labels = models.ManyToManyField(
        Label, through="TaskLabel", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabel(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.PROTECT)