from app.models import Todo
from django.contrib.auth.models import User


def user_get(*, id:int) -> User:
    return User.objects.get(id=id)

def todo_list(*, user_id: int) -> [Todo]:
    todos = Todo.objects.filter(user=user_id).order_by('-created_at')
    return todos
