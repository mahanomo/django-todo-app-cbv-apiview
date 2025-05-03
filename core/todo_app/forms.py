from django.forms import ModelForm
from .models import AddTodo

class TodoForm(ModelForm):
    class Meta:
        model = AddTodo
        fields = "__all__"