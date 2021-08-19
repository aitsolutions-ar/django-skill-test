from django.forms import ModelForm, Textarea, DateInput
from app.models import Todo


class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description','deadline')
        widgets = {
            'deadline': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 5})
        }

class TodoUpdateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'is_done','deadline')
        widgets = {
            'deadline': DateInput(attrs={'class':'form-control', 'type':'date'}),
            'description': Textarea(attrs={'cols': 80, 'rows': 5})
        }