from ast import Is
from asyncio import tasks
from pyexpat import model
from django.http import HttpResponseRedirect

from django.shortcuts import render
from app.forms import TodoForm
from rest_framework import viewsets
from .models import Todo


from app import models
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

def todo_view(request):
    items = models.Todo.objects.filter(user = request.user)
    return render(request, "todo.html", {"items":items})

def add_todo_view(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/app/list/')

    return render(request, "form.html", {'form':form})

def update_todo_view(request, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=todo)
    if todo.user == request.user:
        if request.method == "POST":
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save() 
                return HttpResponseRedirect("/app/list/")
    return render(request, "update.html", {'form':form, 'task':todo})
    