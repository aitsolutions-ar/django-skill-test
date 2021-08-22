from django.db import models
from django.utils import timezone
import datetime

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
    user = models.ForeignKey(
        'auth.User',
        on_delete=models.DO_NOTHING,
        null=True
    )
    #Permite agregar a la clase tiempo limite. No sabia si tenia que ser opcional
    finish_time = models.DateField(
        default= datetime.date.today
    )
