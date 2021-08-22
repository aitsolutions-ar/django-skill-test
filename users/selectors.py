from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def user_get(
    *,
    id: int
) -> User:
    try:
        user = User.objects.get(id=id)
        return user
    except ObjectDoesNotExist:
        return
