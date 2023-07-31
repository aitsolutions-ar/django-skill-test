from .models import Todo

def get_todo_by_id(todo_id):
    try:
        return Todo.objects.get(id=todo_id)
    except Todo.DoesNotExist:
        return None

def get_todos_for_user(user):
    return Todo.objects.filter(user=user).order_by('-created_at')

def create_todo(title, description, user, deadline=None):
    return Todo.objects.create(title=title, description=description, user=user, deadline=deadline)

def update_todo(todo, title=None, description=None, completed=None, deadline=None):
    if title:
        todo.title = title
    if description:
        todo.description = description
    if completed is not None:
        todo.completed = completed
    if deadline:
        todo.deadline = deadline
    todo.save()
    return todo

def delete_todo(todo):
    todo.delete()