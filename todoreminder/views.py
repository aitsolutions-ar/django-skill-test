from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

#AUX FUNCTIONS

def create_user (first_name, last_name, username, email, password):
    new_user = User.objects.create_user(username, email, password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()

    return ("Ok")

def home (request):
    return render (request, 'index.html')

def login (request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        correct_autenticatation = authenticate(username=username, password=password)
        if correct_autenticatation:
            data = User.objects.get(username=username)

            request.session['id'] = data.id
            request.session['name'] = username
            return redirect('/app/')
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

        create_user (first_name, last_name, username, email, password)

        return HttpResponseRedirect("/")

    return render (request, 'singup.html', )
