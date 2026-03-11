from django.urls import path

from .views import (
    StatusCreateView,
    StatusDeleteView,
    StatusIndexView,
    StatusUpdateView,
)

app_name = "statuses"

urlpatterns = [
    path("", StatusIndexView.as_view(), name="index"),
    path("create/", StatusCreateView.as_view(), name="create"),
    path("<int:pk>/update/", StatusUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", StatusDeleteView.as_view(), name="delete"),
]
