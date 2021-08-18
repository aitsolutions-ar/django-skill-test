from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from app import services

def home (request):
    return render (request, 'index.html')

def login (request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = services.authentication(username, password)

        if (user):
            request.session['id'] = user.id
            request.session['name'] = username
            return redirect('/app/1')
        else:
            print("Error, not authenticated")
    return HttpResponseRedirect ("/")    

@csrf_exempt
def singup (request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        services.create_user (first_name, last_name, username, email, password)

        return HttpResponseRedirect("/")

    return render (request, 'singup.html', )
