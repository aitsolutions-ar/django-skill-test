from django.contrib.auth.models import User


def user_create(
    *,
    username: str,
    password: str
) -> User:
    user = User()
    user.username = username
    user.set_password(password)
    user.full_clean()
    user.save()
    return user
