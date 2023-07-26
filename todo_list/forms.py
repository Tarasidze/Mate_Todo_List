from django import forms
from django.contrib.auth.forms import UserCreationForm
from todo_list.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['content', 'deadline_datetime', 'is_done', 'tags']

        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
