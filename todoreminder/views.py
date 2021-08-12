from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render

def home (request):
    return render (request, 'index.html')

def login (request):
    if (request.method == 'POST'):
        print("POST METHOD")
        return HttpResponse ("Hola")
        # Verificar que el usuario esté registrado y mostrar el homepage

    return HttpResponse("hola")

def singup (request):
    if (request.method == 'POST'):
        print("POST METHOD")
        return HttpResponse ("Hola")
        # Registrar el usuario en la base de datos
        # Redireccionar al home
    
    return render (request, 'singup.html')
