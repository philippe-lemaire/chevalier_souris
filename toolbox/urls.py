from django.urls import path

from . import views

app_name = "toolbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("colony/", views.generate_colony, name="generate_colony"),
    path(
        "adventure_site/", views.generate_adventure_site, name="generate_adventure_site"
    ),
]
