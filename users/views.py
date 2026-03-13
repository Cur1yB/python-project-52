from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
import os
from .models import User
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserCreateForm
from .mixins import (
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    ProtectDeleteMixin,
)


class UsersList(ListView):
    model = get_user_model()
    template_name = os.path.join("users", "index.html")
    context_object_name = "users"
    extra_context = {
        "edit": "Изменить",
        "delete": "Удалить",
    }


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserCreateForm
    template_name = "login.html"
    success_url = reverse_lazy("login")
    extra_context = {
        "title": "Регистрация",
        "submit": "Зарегистрировать",
    }
    success_message = "Пользователь успешно зарегистрирован"


class UserUpdateView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UserCreateForm
    template_name = "login.html"
    success_url = reverse_lazy("users:users")
    extra_context = {
        "title": "Изменение пользователя",
        "submit": "Изменить",
    }
    success_message = "Пользователь успешно изменен"


class UserDeleteView(
    CustomLoginRequiredMixin,
    CheckChangePermissionMixin,
    ProtectDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    context_object_name = "user"
    template_name = "users/delete.html"
    success_url = reverse_lazy("users:users")
    extra_context = {
        "title": "Удаление пользователя",
        "submit": "Да, удалить",
        "confirm": "Вы уверены, что хотите удалить",
    }
    success_message = "Пользователь успешно удален"
