from django.urls import path

from .views import (
    index,

    TasksListView,
    TaskCreateView,
    TaskUpdateView,
    UpdateTaskStatusView,
    TasklDeleteView,

    TagsListView,
    TagsCreateView,
    TagsUpdateView,
    TagsDeleteView,

)

urlpatterns = [
    path("", index, name="index"),

    path("tasks/", TasksListView.as_view(), name="tasks-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/update-status/", UpdateTaskStatusView.as_view(), name="update_task_status"),
    path("tasks/<int:pk>/delete/", TasklDeleteView.as_view(), name="task-delete"),

    path("tags/", TagsListView.as_view(), name="tags-list"),
    path("tags/create/", TagsCreateView.as_view(), name="tags-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tags-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tags-delete"),
]

app_name = "todo_list"
