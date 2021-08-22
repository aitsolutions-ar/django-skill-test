from django.urls import path, include

from app.apis import (
    TodoCreateApi,
    TodoDeleteApi,
    TodoDetailApi,
    TodoListApi,
    TodoUpdateApi
)

todo_patterns = [
    path('', TodoListApi.as_view(), name='list'),
    path('create/', TodoCreateApi.as_view(), name='create'),
    path('<int:todo_id>/', TodoDetailApi.as_view(), name='detail'),
    path('<int:todo_id>/update', TodoUpdateApi.as_view(), name='update'),
    path('<int:todo_id>/delete', TodoDeleteApi.as_view(), name='delete'),
]

urlpatterns = [
    path('', include((todo_patterns, 'todos')))
]