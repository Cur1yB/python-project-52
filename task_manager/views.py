from django.views.generic import TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
import os

class IndexView(TemplateView):
    template_name = os.path.join("index.html")

class LoginUser(LoginView):
    template_name = os.path.join("login.html")
    reverse_page = reverse_lazy("home")
    extra_context = {
        "title": "Войти",
        "submit": "Войти",
    }

    def form_valid(self, form):
        messages.info(self.request, "Вы залогинены")
        return super().form_valid(form)

class LogoutUser(LogoutView):
    template_name = os.path.join("logout.html")
    reverse_page = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)