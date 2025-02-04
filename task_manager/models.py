from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django_extensions.management.commands.export_emails import full_name


class UniqueName(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        abstract = True
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Position(UniqueName):
    pass


class TaskType(UniqueName):
    pass


class ProjectType(UniqueName):
    pass


class Team(UniqueName):
    slug = AutoSlugField(
        max_length=100,
        populate_from=["name"]
    )


class Worker(AbstractUser):
    # CATCH IN FORMS
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True
    )
    teams = models.ManyToManyField(
        Team,
        through="WorkerTeam",
        through_fields=("worker", "team", ),
        blank=True
    )

    class Meta:
        default_related_name = "workers"

        verbose_name = "worker"
        verbose_name_plural = "workers"

        ordering = ("username", )

    def get_absolute_url(self):
        return reverse("task_manager:worker-detail", kwargs={"pk": self.pk})

    @property
    def full_name(self) -> str:
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


class BaseToDoItem(models.Model):
    class PriorityLevel(models.IntegerChoices):
        VERY_HIGH = 1, "Urgent"
        HIGH = 2, "High"
        MEDIUM = 3, "Medium"
        LOW = 4, "Low"
        VERY_LOW = 5, "Optional"

    name = models.CharField(max_length=100)
    slug = AutoSlugField(
        max_length=100,
        populate_from=["name"]
    )
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    priority = models.IntegerField(
        PriorityLevel.choices,
        default=PriorityLevel.MEDIUM
    )

    class Meta:
        abstract = True
        ordering = ("is_completed", "-created_at")


class Project(BaseToDoItem):
    project_type = models.ForeignKey(
        ProjectType,
        on_delete=models.CASCADE,
    )
    teams = models.ManyToManyField(
        Team,
        through="ProjectTeam",
        through_fields=("project", "team", ),
        blank=True
    )

    class Meta(BaseToDoItem.Meta):
        default_related_name = "projects"


class Task(BaseToDoItem):
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    workers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="TaskWorker",
        through_fields=("task", "worker"),
        blank=True
    )

    class Meta(BaseToDoItem.Meta):
        default_related_name = "tasks"


class BaseAssignee(models.Model):
    assigned_at = models.DateTimeField(auto_now_add=True)
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="assigned_%(class)s"
    )

    class Meta:
        abstract = True
        ordering = ("assigned_at",)


class WorkerTeam(BaseAssignee):
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    class Meta(BaseAssignee.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "team"],
                name="unique_team_worker_constraint"
            )
        ]


class TaskWorker(BaseAssignee):
    worker = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )

    class Meta(BaseAssignee.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["worker", "task"],
                name="unique_task_worker_constraint",
            )
        ]


class ProjectTeam(BaseAssignee):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
    )

    class Meta(BaseAssignee.Meta):
        constraints = [
            models.UniqueConstraint(
                fields=["team", "project"],
                name="unique_team_project_constraint",
            )
        ]
