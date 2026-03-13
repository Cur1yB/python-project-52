import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LabelForm
from .models import Label
from .mixins import CheckCascadeMixin


class IndexLabelView(LoginRequiredMixin, ListView):
    template_name = os.path.join("labels", "index.html")
    model = Label
    context_object_name = "labels"
    extra_context = {
        "title": "Метки",
        "ID": "ID",
        "name": "Имя",
        "edit": "Изменить",
        "delete": "Удалить",
        "created_at": "Дата создания",
        "submit": "Создать метку",
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels:index")  # <-- правильно
    extra_context = {
        "title": "Создать метку",
        "submit": "Создать",
    }
    success_message = "Метка успешно создана"

class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = os.path.join("labels", "create.html")
    success_url = reverse_lazy("labels:index")
    extra_context = {
        "title": "Изменение метки",
        "submit": "Изменить",
    }
    success_message = "Метка успешно изменена"


class DeleteLabelView(LoginRequiredMixin, CheckCascadeMixin, SuccessMessageMixin, DeleteView):
    model = Label
    context_object_name = "label"
    template_name = os.path.join("labels", "delete.html")
    success_url = reverse_lazy("labels:index")
    extra_context = {
        "title": "Удаление метки",
        "submit": "Да, удалить",
        "confirm": "Вы уверены, что хотите удалить",
    }
    success_message = "Метка успешно удалена"
    protected_error_message = "Невозможно удалить метку, потому что она используется"