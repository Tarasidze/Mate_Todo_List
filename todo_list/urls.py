from django.urls import path

from .views import (
    index,
    TasksListView,
    TaskCreateView,
    TasklDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", TasksListView.as_view(), name="tasks-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/delete/", TasklDeleteView.as_view(), name="task-delete"),

]

app_name = "todo_list"
