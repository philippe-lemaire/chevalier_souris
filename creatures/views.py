import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Creature

# Create your views here.


class IndexView(generic.ListView):
    model = Creature
    ordering = ["name"]


class CreatureDetailView(generic.DetailView):
    model = Creature

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["roll"] = random.randint(1, 6)
        return context
