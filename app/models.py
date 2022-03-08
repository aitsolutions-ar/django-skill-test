import datetime
from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(
        max_length=32
    )
    description = models.CharField(
        max_length=128,
        null=False
    )
    is_done = models.BooleanField(
        default=False
    )
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.DO_NOTHING,
        null = True,
        blank = True
    )
    time = models.DateTimeField(
        default= datetime.datetime.now
    )
   