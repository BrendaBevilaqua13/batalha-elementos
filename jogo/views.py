from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Carta
import random


baralho_maquina = []
baralho_user = []
nome = ''


def batalha(request):
    global nome
    global baralho_maquina
    global baralho_user
    global embaralhar
    if request.method == 'POST':
        nome = request.POST['nome'].strip()

        if len(nome) == 0 or len(nome) > 8:
            return render(request, 'index.html')
        
        cartas = Carta.objects.all()

        while len(baralho_maquina) < 5:
            elemento = random.choice(cartas)
            if elemento in baralho_maquina:
                continue
            baralho_maquina.append(elemento)
            
        while len(baralho_user)< 5:
            elemento2 = random.choice(cartas)
            if elemento2 in baralho_user:
                continue
            baralho_user.append(elemento2) 
              
        context = {
            'nome': nome.strip().capitalize(),
            'baralho_maquina': baralho_maquina,
            'baralho_user': baralho_user,
        }
        return render(request, 'batalha.html', context)

           

def teste(request, id):
    global nome
    global baralho_maquina
    global baralho_user
    
    carta = get_object_or_404(Carta,pk=id)
    context = {
        'carta': carta,
        'nome': nome,
        'baralho_maquina': baralho_maquina,
        'baralho_user': baralho_user,
    }
    return render(request, 'batalha.html', context)
            