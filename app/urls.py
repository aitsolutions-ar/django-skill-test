from django.urls import path
from .views import TodoListCreateView, TodoRetrieveUpdateDeleteView


urlpatterns = [
    path('todos/', TodoListCreateView.as_view(), name='todo-list-create'),
    path('todos/<int:id>/', TodoRetrieveUpdateDeleteView.as_view(), name='todo-retrieve-update-delete'),
]