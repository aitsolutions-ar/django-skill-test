from django.urls import path, include

from users.apis import UserCreateApi

user_patterns = [
    path('register/', UserCreateApi.as_view(), name='register-user')
]

urlpatterns = [
    path('', include((user_patterns, 'users')))
]