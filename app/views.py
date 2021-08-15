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
    return render(request, 'dashboard.html')