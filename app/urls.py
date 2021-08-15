from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewset
from .views import app_view

router = DefaultRouter()

router.register('', TodoViewset)

urlpatterns = [
    path('todos/', include(router.urls)),
    path('', app_view, name='app_view')
]
