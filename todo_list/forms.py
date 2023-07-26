from django import forms
from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['content', 'deadline_datetime', 'is_done', 'tags']

        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
