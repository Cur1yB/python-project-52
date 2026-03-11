from django.urls import path

from .views import (
    TaskCreateView,
    TaskDeleteView,
    TaskDetail,
    TaskIndexView,
    TaskUpdateView,
)

app_name = "tasks"

urlpatterns = [
    path("", TaskIndexView.as_view(), name="index"),
    path("<int:pk>/", TaskDetail.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="delete"),
]