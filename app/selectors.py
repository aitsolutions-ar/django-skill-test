from app.models import Todo
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied



def user_get(
    *,
    id: int
) -> User:
    try:
        user = User.objects.get(id=id)
        return user
    except ObjectDoesNotExist:
        return


def todo_list(
    *,
    user_id: int
) -> [Todo]:
    todos = Todo.objects.filter(user=user_id).order_by('-created_at')
    return todos


def todo_get(
    *,
    fetched_by:User,
    todo_id: int
) -> Todo:
    try:
        todo = Todo.objects.get(id=todo_id)
        if fetched_by == todo.user:
            return todo
        else:
            raise PermissionDenied
    except ObjectDoesNotExist:
        raise PermissionDenied