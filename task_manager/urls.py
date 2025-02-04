from django.urls import path

from task_manager.views import (
    index,
    TaskTypeListView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
    ProjectTypeListView,
    ProjectTypeCreateView,
    ProjectTypeUpdateView,
    ProjectTypeDeleteView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
    PositionListView,
    WorkerListView,
    WorkerCreateView,
    WorkerDetailView,
    WorkerUpdateView,
    WorkerDeleteView,
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    AssignWorkerToTaskView,
    ToggleTaskStatus,
)

urlpatterns = [
    path("", index, name="index"),
    # TaskType views
    path(
        "task-types/",
        TaskTypeListView.as_view(),
        name="task-type-list",
    ),
    path(
        "task-types/create/",
        TaskTypeCreateView.as_view(),
        name="task-type-create",
    ),
    path(
        "task-types/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="task-type-update",
    ),
    path(
        "task-types/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="task-type-delete",
    ),
    # ProjectType views
    path(
        "project-types/",
        ProjectTypeListView.as_view(),
        name="project-type-list",
    ),
    path(
        "project-types/create/",
        ProjectTypeCreateView.as_view(),
        name="project-type-create",
    ),
    path(
        "project-types/<int:pk>/update/",
        ProjectTypeUpdateView.as_view(),
        name="project-type-update",
    ),
    path(
        "project-types/<int:pk>/delete/",
        ProjectTypeDeleteView.as_view(),
        name="project-type-delete",
    ),
    # Position views
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "positions/<int:pk>/update",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "positions/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
    # Worker views
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    # Task views
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "tasks/<int:pk>/assign-worker/",
        AssignWorkerToTaskView.as_view(),
        name="assign-worker-to-task",
    ),
    path(
        "tasks/<int:pk>/toggle-status/",
        ToggleTaskStatus.as_view(),
        name="task-toggle-status",
    ),
]

app_name = "task_manager"
