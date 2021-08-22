from app.models import Todo
from app.selectors import user_get, todo_get
from django.contrib.auth.models import User


def todo_create(
    *,
    user_id: int,
    title: str,
    description:str,
    is_done: bool,
) -> Todo:
    current_user = user_get(id=user_id)
    todo = Todo(title=title,
                description=description,
                is_done=is_done,
                user=current_user
                )
    todo.full_clean()
    todo.save()
    return todo


def todo_markasdone(
    *,
    fetched_by: User,
    todo_id: int,
    is_done: bool
) -> Todo:
    todo = todo_get(fetched_by=fetched_by, todo_id=todo_id)
    todo.is_done = is_done
    todo.full_clean()
    todo.save()
    return todo