from ast import Is
from rest_framework import viewsets

from app import models
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated

class TodoViewset(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)