from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def articles(request, year):
    return HttpResponse('O ano enviado foi: ' +str(year))

def lerBanco(nome):
    listaNomes = [
        {'nome':'Teste', 'idade':27},
        {'nome':'Teste2', 'idade':18},
        {'nome':'Marcelo','idade':20}
    ]

    for pessoa in listaNomes:
        if pessoa['nome'] == nome:
            return pessoa
        else:
            return {'nome':'Nada Encontrado'}

def fname2(request, nome):
    result = lerBanco(nome)
    return render(request, 'pessoa.html', {'vIdade': result})
