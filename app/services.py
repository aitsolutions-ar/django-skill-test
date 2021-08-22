from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import requests
import datetime

from app import models

def create_user (first_name, last_name, username, email, password):
    new_user = User.objects.create_user(username, email, password)
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.save()

    return ("Ok")

def add_todo (title, description, is_done, user, finish_time):
    url = 'http://127.0.0.1:8000/app/todos/'

    todo = {
        'title': title,
        'description': description,
        'is_done': is_done,
        'user': user,
        'finish_time': finish_time,
    }
    
    requests.post(url, data=todo)

def done_todo (todo_id):
    todo = models.Todo.objects.filter(id=todo_id).update(is_done=True)

def get_todos (user, username):
    todos = models.Todo.objects.filter(user_id=user).order_by('-id')

    todos_list = []
    for todo in todos:
        task = {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'is_done': todo.is_done,
            'user_id': todo.user_id,
            'finish_time': todo.finish_time
        }
        todos_list.append(task)
    
    return todos_list

def authentication (username, password):
    correct_autenticatation = authenticate(username=username, password=password)

    if correct_autenticatation:
        data = User.objects.get(username=username)
    else:
        data = None
    
    return data