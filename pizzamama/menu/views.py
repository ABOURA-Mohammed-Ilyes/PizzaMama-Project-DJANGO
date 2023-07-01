from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_noms = [pizza.nom for pizza in pizzas]
    pizzas_noms_str = ", ".join(pizzas_noms)
    return HttpResponse("Les pizzas : " + pizzas_noms_str)