import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy as reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from tasks.filter import TaskFilter
from tasks.forms import TaskForm
from tasks.mixins import AuthorRequireMixin
from tasks.models import Task
from users.models import User

_UI_ACTIONS = {
    "edit": "Изменить",
    "delete": "Удалить",
}

_TASK_LIST_COLUMNS = {
    "ID": "ID",
    "name": "Имя",
    "status": "Статус",
    "author": "Автор",
    "executor": "Исполнитель",
    "select": "Выбрать",
    "created_at": "Дата создания",
}

_ROUTES = {
    "tasks_index": "tasks:index",
}

class TaskIndexView(LoginRequiredMixin, FilterView, ListView):
    model = Task
    filterset_class = TaskFilter
    template_name = os.path.join("tasks", "index.html")
    context_object_name = "tasks"
    extra_context = {
        "title": "Задачи",
        **_TASK_LIST_COLUMNS,
        **_UI_ACTIONS,
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = TaskForm
    template_name = os.path.join("tasks", "create.html")
    success_url = reverse(_ROUTES["tasks_index"])
    extra_context = {
        "title": "Создать задачу",
        "submit": "Создать",
    }
    success_message = "Задача успешно создана"
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = User.objects.get(pk=user.pk)
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = os.path.join("tasks", "create.html")
    success_url = reverse(_ROUTES["tasks_index"])
    extra_context = {
        "title": "Изменение задачи",
        "submit": _UI_ACTIONS["edit"],
    }
    success_message = "Задача успешно изменена"
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class TaskDeleteView(
    LoginRequiredMixin, AuthorRequireMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = os.path.join("tasks", "delete.html")
    context_object_name = "task"
    success_url = reverse(_ROUTES["tasks_index"])
    extra_context = {
        "title": "Удаление задачи",
        "submit": "Да, удалить",
        "confirm": "Вы уверены, что хотите удалить",
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE
    success_message = "Задача успешно удалена"


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = os.path.join("tasks", "detail.html")
    extra_context = {
        "title": "Просмотр задачи",
        "author": "Автор",
        "executor": "Исполнитель",
        "status": "Статус",
        "created": "Дата создания",
        "labels": "Метки",
        **_UI_ACTIONS,
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE
