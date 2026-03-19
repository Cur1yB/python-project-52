import os

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import StatusForm
from .mixins import CheckCascadeMixin
from .models import Status

_INDEX_PAGE = "statuses:index"

# Common UI strings (single source of truth)
_UI_ACTIONS = {
    "edit": "Изменить",
    "delete": "Удалить",
}

_UI_COMMON = {
    "ID": "ID",
    "name": "Имя",
    "created_at": "Дата создания",
}

_TITLE_INDEX = "Статусы"
_TITLE_CREATE = "Создать статус"
_TITLE_UPDATE = "Изменение статуса"
_TITLE_DELETE = "Удаление статуса"

_SUBMIT_CREATE = "Создать"
_SUBMIT_DELETE = "Да, удалить"

_CONFIRM_DELETE = "Вы уверены, что хотите удалить"

_SUCCESS_CREATED = "Статус успешно создан"
_SUCCESS_UPDATED = "Статус успешно изменен"
_SUCCESS_DELETED = "Статус успешно удален"

_PROTECTED_ERROR_MESSAGE = "Невозможно удалить статус, " \
"потому что он используется"


class StatusIndexView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "index.html")
    extra_context = {
        "title": _TITLE_INDEX,
        **_UI_COMMON,
        **_UI_ACTIONS,
        "create_status": _TITLE_CREATE,
    }
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "create.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_CREATE,
        "submit": _SUBMIT_CREATE,
    }
    success_message = _SUCCESS_CREATED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    context_object_name = "statuses"
    template_name = os.path.join("statuses", "create.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_UPDATE,
        "submit": _UI_ACTIONS["edit"],
    }
    success_message = _SUCCESS_UPDATED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE


class StatusDeleteView(
    LoginRequiredMixin, CheckCascadeMixin, SuccessMessageMixin, DeleteView
):
    model = Status
    context_object_name = "status"
    template_name = os.path.join("statuses", "delete.html")
    success_url = reverse_lazy(_INDEX_PAGE)
    extra_context = {
        "title": _TITLE_DELETE,
        "confirm": _CONFIRM_DELETE,
        "submit": _SUBMIT_DELETE,
    }
    success_message = _SUCCESS_DELETED
    permission_denied_message = settings.LOGIN_REQUIRED_MESSAGE
    protected_error_message = _PROTECTED_ERROR_MESSAGE
