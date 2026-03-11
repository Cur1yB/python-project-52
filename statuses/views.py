from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

import os

from .forms import StatusForm
from .models import Status
from .mixins import CheckCascadeMixin


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "index.html")
    extra_context = {
        "title": "Статусы",
        "ID": "ID",
        "name": "Имя",
        "edit": "Изменить",
        "delete": "Удалить",
        "created_at": "Дата создания",
        "create_status": "Создать статус",
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "create.html")
    success_url = reverse_lazy("statuses:index")
    extra_context = {
        "title": "Создать статус",
        "submit": "Создать",
    }
    success_message = "Статус успешно создан"
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "create.html")
    success_url = reverse_lazy("statuses:index")
    extra_context = {
        "title": "Изменение статуса",
        "submit": "Изменить",
    }
    success_message = "Статус успешно изменен"
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusDeleteView(LoginRequiredMixin, CheckCascadeMixin, SuccessMessageMixin, DeleteView):
    model = Status
    context_object_name = "status"
    template_name = os.path.join("statuses", "delete.html")
    success_url = reverse_lazy("statuses:index")
    extra_context = {
        "title": "Удаление статуса",
        "confirm": "Вы уверены, что хотите удалить",
        "submit": "Да, удалить",
    }
    success_message = "Статус успешно удален"
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE
    protected_error_message = "Невозможно удалить статус, потому что он используется"