import os

from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserCreateForm
from .mixins import (
    CheckChangePermissionMixin,
    CustomLoginRequiredMixin,
    ProtectDeleteMixin,
)
from .models import User

# Common UI strings
_UI_ACTIONS = {
    "edit": "Изменить",
    "delete": "Удалить",
}

_CONFIRM_DELETE = "Вы уверены, что хотите удалить"
_SUBMIT_DELETE = "Да, удалить"

_TEMPLATE_USERS_INDEX = os.path.join("users", "index.html")
_TEMPLATE_USER_FORM = "login.html"
_TEMPLATE_USER_DELETE = os.path.join("users", "delete.html")

_ROUTE_LOGIN = "login"
_ROUTE_USERS_LIST = "users:users"

_TITLE_REGISTER = "Регистрация"
_TITLE_UPDATE = "Изменение пользователя"
_TITLE_DELETE = "Удаление пользователя"

_SUBMIT_REGISTER = "Зарегистрировать"
_SUBMIT_UPDATE = _UI_ACTIONS["edit"]

_SUCCESS_REGISTERED = "Пользователь успешно зарегистрирован"
_SUCCESS_UPDATED = "Пользователь успешно изменен"
_SUCCESS_DELETED = "Пользователь успешно удален"


class UsersList(ListView):
    model = get_user_model()
    template_name = _TEMPLATE_USERS_INDEX
    context_object_name = "users"
    extra_context = {
        **_UI_ACTIONS,
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = _TEMPLATE_USER_FORM
    success_url = reverse_lazy(_ROUTE_LOGIN)
    extra_context = {
        "title": _TITLE_REGISTER,
        "submit": _SUBMIT_REGISTER,
    }
    success_message = _SUCCESS_REGISTERED


class UserUpdateView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserCreateForm
    template_name = _TEMPLATE_USER_FORM
    success_url = reverse_lazy(_ROUTE_USERS_LIST)
    extra_context = {
        "title": _TITLE_UPDATE,
        "submit": _SUBMIT_UPDATE,
    }
    success_message = _SUCCESS_UPDATED


class UserDeleteView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    context_object_name = "user"
    template_name = _TEMPLATE_USER_DELETE
    success_url = reverse_lazy(_ROUTE_USERS_LIST)
    extra_context = {
        "title": _TITLE_DELETE,
        "submit": _SUBMIT_DELETE,
        "confirm": _CONFIRM_DELETE,
    }
    success_message = _SUCCESS_DELETED
