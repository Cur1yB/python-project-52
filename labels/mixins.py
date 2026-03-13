from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect


class CheckCascadeMixin:
    protected_error_message = "Невозможно удалить метку, " \
        "потому что она используется."

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, self.protected_error_message)
        return redirect(self.success_url)
