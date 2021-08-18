from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import requests

from app import models
from app import services
from .serializers import TodoSerializer


class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer

@csrf_exempt
def app_view (request, page):
    user = request.session['id']
    username = request.session['name']
    todos = services.get_todos(user, username)
    page_todo = Paginator(todos, 5)
    amount_pages = page_todo.num_pages

    selected_page = page_todo.page(page)

    next_page = 0
    prev_page = 0

    if (page < amount_pages):
        next_page = page + 1
    if (page >= 2):
        prev_page = page - 1

    ctx = {
        'username': username,
        'user_id': user,
        'todos': selected_page.object_list,
        'amount_pages': amount_pages,
        'current_page': page,
        'next_page': next_page,
        'prev_page': prev_page
    }
    print(ctx)
    return render(request, 'dashboard.html', ctx)

def add_todo(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        is_done = False
        user = request.session['id']

        services.add_todo(title, description, is_done, user)

        return HttpResponseRedirect("/app/1")
    return render (request, 'add_todo.html')

def done (request, todo_id):
    services.done_todo(todo_id)
    return HttpResponseRedirect("/app/1")

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")