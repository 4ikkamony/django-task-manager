from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic

from task_manager.mixins import (
    NameSearchMixin,
    ToDoItemSearchMixin,
    WorkerSearchMixin,
)
from task_manager.forms import (
    WorkerCreationForm,
    TaskForm,
    TaskWorkersUpdateForm,
)
from task_manager.models import (
    Team,
    Worker,
    Project,
    Task,
    Position,
    TaskType,
    ProjectType,
    TaskWorker,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "task_manager/index.html")


class TaskTypeListView(
    LoginRequiredMixin,
    NameSearchMixin,
    generic.ListView
):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "task_manager/task_type_list.html"
    paginate_by = 5


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    template_name = "task_manager/task_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:task-type-list")
    context_object_name = "task_type"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-type-list")
    context_object_name = "task_type"


class ProjectTypeListView(
    LoginRequiredMixin,
    NameSearchMixin,
    generic.ListView
):
    model = ProjectType
    context_object_name = "project_type_list"
    template_name = "task_manager/project_type_list.html"
    paginate_by = 5


class ProjectTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = ProjectType
    template_name = "task_manager/project_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-type-list")


class ProjectTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ProjectType
    template_name = "task_manager/project_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-type-list")
    context_object_name = "project_type"


class ProjectTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ProjectType
    template_name = "task_manager/project_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:project-type-list")
    context_object_name = "project_type"


class PositionListView(
    LoginRequiredMixin,
    NameSearchMixin,
    generic.ListView
):
    model = Position
    paginate_by = 5


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")


class WorkerListView(
    LoginRequiredMixin,
    WorkerSearchMixin,
    generic.ListView
):
    model = Worker
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.select_related("position")


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "position",
        "teams",
    )
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(
    LoginRequiredMixin,
    ToDoItemSearchMixin,
    generic.ListView
):
    model = Task
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related("workers", "taskworker_set__worker")
        return queryset


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("task_manager:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task_manager:task-list")


class TaskWorkersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskWorkersUpdateForm
    success_url = reverse_lazy("task_manager:task-list")


@login_required
def unassign_worker_from_task(request, task_id, worker_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        worker = get_object_or_404(Worker, id=worker_id)
        if task in worker.tasks.all():
            worker.tasks.remove(task_id)
    return HttpResponseRedirect(reverse_lazy("task_manager:task-list"))


@login_required
def toggle_task_status(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, id=pk)
        if task.is_completed:
            task.is_completed = False
            task.completed_at = None
        else:
            task.is_completed = True
            task.completed_at = timezone.now()
        task.save()
    return HttpResponseRedirect(reverse_lazy("task_manager:task-list"))
