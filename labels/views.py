import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LabelForm
from .mixins import CheckCascadeMixin
from .models import Label

_INDEX_PAGE = "labels:index"

_UI_ACTIONS = {
    "edit": "Изменить",
    "delete": "Удалить",
}

_UI_COMMON = {
    "ID": "ID",
    "name": "Имя",
    "created_at": "Дата создания",
}

_TITLE_INDEX = "Метки"
_TITLE_CREATE = "Создать метку"
_TITLE_UPDATE = "Изменение метки"
_TITLE_DELETE = "Удаление метки"

_SUBMIT_CREATE = "Создать"
_SUBMIT_DELETE = "Да, удалить"

_CONFIRM_DELETE = "Вы уверены, что хотите удалить"

_SUCCESS_CREATED = "Метка успешно создана"
_SUCCESS_UPDATED = "Метка успешно изменена"
_SUCCESS_DELETED = "Метка успешно удалена"

_PROTECTED_ERROR_MESSAGE = (
    "Невозможно удалить метку, потому что она используется"
)


class IndexLabelView(LoginRequiredMixin, ListView):
    template_name = os.path.join("labels", "index.html")
    model = Label
    context_object_name = "labels"
    extra_context = {
        "title": _TITLE_INDEX,
        **_UI_COMMON,
        **_UI_ACTIONS,
        "submit": _TITLE_CREATE,
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class CreateLabelView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = os.path.join("labels", "create.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_CREATE,
        "submit": _SUBMIT_CREATE,
    }
    success_message = _SUCCESS_CREATED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class UpdateLabelView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = os.path.join("labels", "create.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_UPDATE,
        "submit": _UI_ACTIONS["edit"],
    }
    success_message = _SUCCESS_UPDATED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class DeleteLabelView(
    LoginRequiredMixin,
    CheckCascadeMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    context_object_name = "label"
    template_name = os.path.join("labels", "delete.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_DELETE,
        "submit": _SUBMIT_DELETE,
        "confirm": _CONFIRM_DELETE,
    }
    success_message = _SUCCESS_DELETED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE
    protected_error_message = _PROTECTED_ERROR_MESSAGE
