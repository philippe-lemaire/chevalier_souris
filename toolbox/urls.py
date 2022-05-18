from django.urls import path

from . import views

app_name = "toolbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("colonie_de_souris/", views.generate_colony, name="generate_colony"),
    path(
        "site_d_aventure/",
        views.generate_adventure_site,
        name="generate_adventure_site",
    ),
    path("souris_non_joueuse/", views.generate_npc_mouse, name="generate_npc_mouse"),
    path("graine_d_aventure/", views.generate_seed, name="generate_seed"),
    path("trouver_un_sort/", views.generate_spell, name="generate_spell"),
    path(
        "trouver_une_épée_magique/",
        views.generate_magic_sword,
        name="generate_magic_sword",
    ),
    path(
        "créer_une_souris_joueuse/",
        views.generate_mouse_pc,
        name="generate_mouse_pc",
    ),
]
