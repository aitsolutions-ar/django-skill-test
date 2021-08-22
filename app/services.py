from datetime import datetime
from django.contrib.auth.models import User
from app.models import Todo
from app.selectors import todo_get
from users.selectors import user_get


def todo_create(
    *,
    user_id: int,
    title: str,
    description: str,
    is_done: bool,
    completion_deadline: datetime
) -> Todo:
    current_user = user_get(id=user_id)
    todo = Todo(title=title,
                description=description,
                is_done=is_done,
                user=current_user,
                completion_deadline=completion_deadline
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


def todo_delete(
    *,
    fetched_by: User,
    todo_id: int
) -> Todo:
    todo = todo_get(fetched_by=fetched_by, todo_id=todo_id)
    todo.delete()
