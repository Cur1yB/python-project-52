from django.urls import path
from .views import (
    UsersList,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

app_name = "users"

urlpatterns = [
    path("", UsersList.as_view(), name="users"),
    path("create/", UserCreateView.as_view(), name="create"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete"),
]
