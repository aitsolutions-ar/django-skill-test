from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.CharField(
        max_length=128,
        null=True
    )
    is_done = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    deadline = models.DateTimeField(
        null=True, blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
