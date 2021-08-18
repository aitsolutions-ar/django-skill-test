from django.forms import ModelForm, Textarea
from app.models import Todo


class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 5})
        }

class TodoUpdateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_done')
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 5})
        }