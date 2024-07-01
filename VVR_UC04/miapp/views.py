from django.shortcuts import render


# Create your views here.

def integrantes(request):
    return render(request, 'integrantes.html',{
        'titulo': 'Integrantes'
    })
    

def saludo(request):
    return render(request, 'saludo.html',{
        'titulo': 'Saludo'
    })