from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.contrib.auth import get_user_model
import os

class UsersList(ListView):
    model = get_user_model()
    template_name = os.path.join('users', 'index.html')
    context_object_name = 'users'
