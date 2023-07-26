from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.views.generic import FormView, CreateView
from django.urls import reverse_lazy

from todo_list.forms import TaskForm
from todo_list.models import Task


@login_required
def index(request):
    num_tasks = Task.objects.count()
    num_task_in_progress = Task.objects.filter(is_done=False).count()

    context = {
        "num_tasks": num_tasks,
        "num_task_in_progress": num_task_in_progress,
    }

    return render(request, "todo_list/index.html", context=context)


class TasksListView(LoginRequiredMixin, generic.ListView):
    model = Task
    pagination = 10
    context_object_name = "tasks_list"
    template_name = "todo_list/tasks_list.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_list/task_form.html"
    success_url = reverse_lazy("todo_list:tasks-list")


class TasklDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:tasks-list")


