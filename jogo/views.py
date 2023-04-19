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
            baralho.append(elemento)
        
        print(len(baralho))
        for i in baralho:
            print(i.elemento)
            
            
    
        context = {
            'nome': nome.strip().capitalize(),
            'cartas': cartas,
        }

        return render(request, 'batalha.html', context)
