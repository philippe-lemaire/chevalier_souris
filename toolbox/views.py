from django.shortcuts import render
from django.http import HttpResponse
from .game_logic.colony import generate_colony_obj
from .game_logic.adventure_site import generate_adventure_site_obj
from .game_logic.npc import NPC_Mouse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the toolbox index.</h1>")


def generate_colony(request):
    # view logic here

    context = {"colony": generate_colony_obj()}
    return render(request, "toolbox/generate_colony.html", context)


def generate_adventure_site(request):
    context = {"site": generate_adventure_site_obj()}
    return render(request, "toolbox/generate_adventure_site.html", context)


def generate_npc_mouse(request):
    npc = NPC_Mouse()
    context = {"npc": npc}
    return render(request, "toolbox/generate_npc_mouse.html", context)
