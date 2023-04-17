from django.shortcuts import render, HttpResponse, redirect


def login(request):
    if request.method == 'POST':
        nome = request.POST['nome'].strip()

        if len(nome) == 0:
            return render(request, 'index.html')

        context = {
            'nome': nome.strip()
        }

        return render(request, 'batalha.html', context)
