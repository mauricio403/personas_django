from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.

def bienvenido(request):
    return HttpResponse('Hola mundo desde Django')


def despedirse(request):
    return HttpResponse('Desedida desde Django')


def contactos(request):
    return HttpResponse('Nombre: Mauricio Matango, Celular: 0960886616')
