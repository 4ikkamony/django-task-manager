from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import WorkerCreationForm
from task_manager.models import (
    Team,
    Worker,
    Project,
    Task,
    Position,
    TaskType,
    ProjectType,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "task_manager/index.html")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
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


class ProjectTypeListView(LoginRequiredMixin, generic.ListView):
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


class PositionListView(LoginRequiredMixin, generic.ListView):
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


class WorkerListView(LoginRequiredMixin, generic.ListView):
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
