from django.urls import path

from . import views

app_name = "toolbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("colony/", views.generate_colony, name="generate_colony"),
]
