from django.urls import path

from .views import Home, submit, update

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("submit", submit, name="submit"),
    path("update", update, name="update"),
]