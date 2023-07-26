from django import forms
from todo_list.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Task
        # fields = "__all__"
        fields = ['content', 'deadline_datetime', 'tags']

        widgets = {
            'deadline_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
