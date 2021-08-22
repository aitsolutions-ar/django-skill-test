"""todoreminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from app.apis import(
    TodoListApi,
    TodoCreateApi,
    TodoDetailApi,
    TodoUpdateApi,
    TodoDeleteApi
)

todo_patterns = [
    path('', TodoListApi.as_view(), name='list'),
    path('create/', TodoCreateApi.as_view(), name='create'),
    path('<int:todo_id>/', TodoDetailApi.as_view(), name='detail'),
    path('<int:todo_id>/update', TodoUpdateApi.as_view(), name='update'),
    path('<int:todo_id>/delete', TodoDeleteApi.as_view(), name='delete'),
]


urlpatterns = [
    path('todos/', include((todo_patterns, 'todos'))),
    path('api-auth/', include('rest_framework.urls')),
]
