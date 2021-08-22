from app.models import Todo
from app.selectors import user_get


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