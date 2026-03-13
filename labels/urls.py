from django.urls import path

from labels.views import (
    CreateLabelView,
    DeleteLabelView,
    IndexLabelView,
    UpdateLabelView,
)

app_name = "labels"

urlpatterns = [
    path("", IndexLabelView.as_view(), name="index"),
    path("create/", CreateLabelView.as_view(), name="create"),
    path("<int:pk>/update/", UpdateLabelView.as_view(), name="update"),
    path("<int:pk>/delete/", DeleteLabelView.as_view(), name="delete"),
]
