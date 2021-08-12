from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render

#AUX FUNCTIONS

def create_user (first_name, last_name, username, email, password):
    #Registrar usuario en base de datos
    return 0

def home (request):
    return render (request, 'index.html')

def login (request):
    if (request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']

        if (validate (email, password)):
            return HttpResponseRedirect("")
        else :
            return HttpResponse("User not found")

def singup (request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        create_user (first_name, last_name, username, email, password)

        return HttpResponseRedirect("/")

    return render (request, 'singup.html')
