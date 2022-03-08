from ast import Is
from asyncio import tasks
from pyexpat import model
from time import time
from turtle import title
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from app.forms import TodoForm
from rest_framework import viewsets
from .models import Todo

from app import models
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

def todo_view(request):
    items = models.Todo.objects.filter(user = request.user).order_by('-time')
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
    try:
        todo = Todo.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/app/registro/")
    if not todo.user.id == request.user.id:
        return HttpResponseRedirect("/app/registro/")
    form = TodoForm(request.POST or None, instance=todo)
    if todo.user == request.user:
        if request.method == "POST":
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save() 
                return HttpResponseRedirect("/app/list/")
    return render(request, "update.html", {'form':form, 'task':todo})
    
#6
class TodoRegister(FormView):
    template_name  = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Todo')

    def form_valid(self, form):
        user = form.save()
        if user != None:
            login(self.request, user)

        return super(TodoRegister,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')

        return self.render_to_response(self.get_context_data())


