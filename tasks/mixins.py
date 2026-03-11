from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy as reverse


class AuthorRequireMixin(UserPassesTestMixin):
    author_require_message = "Задачу может удалить только ее автор"
    redirect_url = reverse("tasks:index")

    def test_func(self):
        return self.get_object().author.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, self.author_require_message)
        return redirect(self.redirect_url)