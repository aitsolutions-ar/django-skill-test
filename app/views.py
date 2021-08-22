from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.core.paginator import Paginator
import requests



from app import models, services
from .serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


def app_view (request, page):
    user = request.session['id']
    username = request.session['name']
    todos = services.get_todos(user, username)
    page_todo = Paginator(todos, 10)
    cant_pages = page_todo.num_pages

    selected_page = page_todo.page(page)

    next_page = 0
    prev_page = 0

    if (page < cant_pages):
        next_page = page + 1
    if (page >= 2):
        prev_page = page - 1

    ctx = {
        'username': username,
        'user_id': user,
        'todos': selected_page.object_list,
        'cant_pages': cant_pages,
        'current_page': page,
        'next_page': next_page,
        'prev_page': prev_page
    }
    print(ctx)
    return render(request, 'main.html', ctx)


## crea la pagina para hacer el posteo de datos.
def add_todo(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        is_done = False
        user = request.session['id']
        finish_time = request.POST['finish_time']

        services.add_todo(title, description, is_done, user, finish_time)
            


        return HttpResponseRedirect("/app/1")
    return render (request, 'todo.html')

#funcion para marcar como completada la task
def done (request, todo_id):
    services.done_todo(todo_id)
    return HttpResponseRedirect("/app/1")

#funcion para desloguearse
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")