from django import forms
from . models import AddTask
class TaskForm(forms.ModelForm):
    class Meta:
        model = AddTask
        fields = ['title', 'catagory', 'status', 'description']
