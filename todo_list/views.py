from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
