from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import requests

from app import models
from app import services
from .serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

@csrf_exempt
def app_view (request):
    user = request.session['id']
    username = request.session['name']
    ctx = services.get_todos(user, username)
    return render(request, 'dashboard.html', ctx)

def add_todo(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        is_done = False
        user = request.session['id']

        services.add_todo(title, description, is_done, user)

        return HttpResponseRedirect("/app/")
    return render (request, 'add_todo.html')

def done (request, todo_id):
    services.done_todo(todo_id)
    return HttpResponseRedirect("/app/")

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")