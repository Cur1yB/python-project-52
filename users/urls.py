from django.urls import path
from .views import ListView

app_name = "users"

urlpatterns = [
    path('', ListView.as_view(), name="users"),
]

