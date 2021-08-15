from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('', TodoViewset)

urlpatterns = [
    path('todos/', include(router.urls)),
    path('', app_view, name='app_view'),
    path('addtodo/', add_todo, name='add_todo'),
    path('logout/', log_out, name='log_out'),
    path('done/<int:todo_id>', done, name='done')
]
