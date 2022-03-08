from dataclasses import fields
from msilib.schema import Class
from django import forms

from app.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_done']