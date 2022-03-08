from posixpath import basename
from unicodedata import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset, add_todo_view, todo_view, update_todo_view

router = DefaultRouter()

router.register('', TodoViewset)

urlpatterns = [
    path('todos/', include(router.urls)),
    path('list/', todo_view, name = 'Todo'),
    path('add/', add_todo_view),
    path('update/<int:id>/', update_todo_view)
]
