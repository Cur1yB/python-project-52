import os

from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

_HOME_PAGE = "home"

_TEMPLATE_INDEX = "index.html"
_TEMPLATE_LOGIN = "login.html"
_TEMPLATE_LOGOUT = "logout.html"

_TITLE_LOGIN = "Войти"
_SUBMIT_LOGIN = "Войти"

_MSG_LOGGED_IN = "Вы залогинены"
_MSG_LOGGED_OUT = "Вы разлогинены"


class IndexView(TemplateView):
    template_name = os.path.join(_TEMPLATE_INDEX)


class LoginUser(LoginView):
    template_name = os.path.join(_TEMPLATE_LOGIN)
    reverse_page = reverse_lazy(_HOME_PAGE)
    extra_context = {
        "title": _TITLE_LOGIN,
        "submit": _SUBMIT_LOGIN,
    }

    def form_valid(self, form):
        messages.info(self.request, _MSG_LOGGED_IN)
        return super().form_valid(form)


class LogoutUser(LogoutView):
    template_name = os.path.join(_TEMPLATE_LOGOUT)
    reverse_page = reverse_lazy(_HOME_PAGE)

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _MSG_LOGGED_OUT)
        return super().dispatch(request, *args, **kwargs)
