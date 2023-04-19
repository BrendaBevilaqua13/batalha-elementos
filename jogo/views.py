from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Carta
import random


def baralho(request):
    if request.method == 'POST':
        nome = request.POST['nome'].strip()

        if len(nome) == 0:
            return render(request, 'index.html')

        cartas = Carta.objects.all()
        baralho = []
        while len(baralho) < 5:
            elemento = random.choice(cartas)
            if elemento in baralho:
                continue
            baralho.append(elemento)  

        context = {
            'nome': nome.strip().capitalize(),
            'baralho': baralho,
        }

        return render(request, 'batalha.html', context)

def teste(request, id):
    carta = get_object_or_404(Carta,pk=id)
    context = {
        'carta': carta
    }
    return render(request, 'teste.html', context)