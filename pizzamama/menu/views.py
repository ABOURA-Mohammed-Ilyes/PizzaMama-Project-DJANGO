from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def index(request):
    pizzas = Pizza.objects.all()
    pizzas_noms_et_prix = [pizza.nom + " : " + str(pizza.prix) + "$" for pizza in pizzas]
    pizzas_noms_et_prix_str = ", ".join(pizzas_noms_et_prix)
    return HttpResponse("Les pizzas : " + pizzas_noms_et_prix_str)