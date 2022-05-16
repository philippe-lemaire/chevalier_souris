from django.shortcuts import render
from django.http import HttpResponse
from .game_logic.colony import generate_colony_obj
import requests

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world. You're at the toolbox index.</h1>")


def generate_colony(request):
    # view logic here

    context = {"colony": generate_colony_obj()}
    return render(request, "toolbox/generate_colony.html", context)
