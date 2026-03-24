from django import forms
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from labels.models import Label
from statuses.models import Status
from tasks.models import Task
from users.models import User


class TaskFilter(FilterSet):
    status = ModelChoiceFilter(label="Статус", queryset=Status.objects.all())
    executor = ModelChoiceFilter(
        label="Исполнитель",
        queryset=User.objects.all()
    )
    labels = ModelChoiceFilter(label="Метка", queryset=Label.objects.all())
    my_tasks = BooleanFilter(
        label="Только свои задачи",
        widget=forms.CheckboxInput,
        method="get_tasks",
    )

    def get_tasks(self, queryset, _, value):
        tasks = queryset.filter(author_id=self.request.user.id)
        return tasks if value else queryset

    class Meta:
        model = Task
        fields = ("status", "executor", "labels")
