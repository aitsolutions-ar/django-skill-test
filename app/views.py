import re
from django.http.response import Http404
from rest_framework import viewsets

from app import models
from .serializers import TodoSerializer
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.views.generic.edit import FormView, CreateView
from django.views.generic.list import ListView

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.views import APIView
from rest_framework.response import Response

from django.core.exceptions import ObjectDoesNotExist

'''
class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
'''

class TodoLogin(LoginView):
    template_name = 'app/login.html'
    redirect_authenticated_user = True
    success_url = 'todos'
    
    def get_success_url(self):
        return reverse_lazy('todos')


class TodoRegister(FormView):
    template_name  = 'app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        user = form.save()
        if user != None:
            login(self.request, user)

        return super(TodoRegister,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todos')

        return self.render_to_response(self.get_context_data())


class TodoList(LoginRequiredMixin,ListView):
    model = models.Todo
    template_name = 'app/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return models.Todo.objects.filter(user=self.request.user).order_by('-created')
        return models.Todo.objects.filter(user=None)

class TodoDetailJSON(LoginRequiredMixin, APIView):
    def get(self,request,pk):
        user = self.request.user
        try:
            todo = models.Todo.objects.filter(user=self.request.user).get(id=pk)
            serializer = TodoSerializer(todo, many=False)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response("No existe la tarea")
            
