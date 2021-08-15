from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from app import models
from .serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

def app_view (request):
    ctx = {
        'username': request.session['name'],
        'user_id': request.session['id']
    }
    return render(request, 'dashboard.html', ctx)

def add_todo(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        is_done = False
        user_id = request.session['id']

        todo = models.Todo(title=title, description=description, is_done=is_done, user_id=user_id)
        todo.save()
        return HttpResponseRedirect("/app/")
    return render (request, 'add_todo.html')