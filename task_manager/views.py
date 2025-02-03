from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from task_manager.models import (
    Team,
    Worker,
    Project,
    Task,
    Position,
    TaskType,
)


@login_required
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "task_manager/index.html")
