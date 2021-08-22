from django.db import models
from django.utils import timezone


# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.CharField(
        max_length=128
    )
    is_done = models.BooleanField(
        default=False
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.DO_NOTHING,
        null=True
    )
    created_at = models.DateTimeField(
        default=timezone.now
    )
    completion_deadline = models.DateTimeField(
        blank=True,
        null=True
    )
