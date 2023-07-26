from django import forms
from django.contrib.auth.forms import UserCreationForm
from todo_list.models import Task


class TaskForm(forms.ModelForm):
    # content = forms.CharField(
    #     max_length=255,
    #     required=False,
    #     label="",
    #     widget=forms.TextInput(attrs={"placeholder": "content"})
    # )

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['content', 'deadline_datetime', 'is_done', 'tags']

        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
