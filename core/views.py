from django.shortcuts import render
from datetime import date

def natal(request):
    if date.month == 12 and date.day == 25:
        contexto = {'natal':True}
        return render(request, 'natal.html', contexto)
    else:
        contexto = {'natal':False}
        return render(request, 'natal.html', contexto)

def tiradentes(request):
    if date.month == 4 and date.day == 21:
        contexto = {'tiradentes':True}
        return render(request, 'tiradentes.html', contexto)
    else:
        contexto = {'tiradentes':False}
        return render(request, 'tiradentes.html', contexto)