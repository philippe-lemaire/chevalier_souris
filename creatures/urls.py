from django.urls import path

from . import views

app_name = "creatures"

urlpatterns = [
    path("", views.index, name="index"),
]
