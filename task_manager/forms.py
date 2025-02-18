from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils import timezone

from task_manager.models import (
    Team,
    Project,
    Worker,
    Task,
    TaskWorker,
)


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = (
            *UserCreationForm.Meta.fields,
            "first_name",
            "last_name",
            "email",
            "position",
            "teams",
        )
        widgets = {
            "teams": forms.CheckboxSelectMultiple(
                attrs={"class": "form-select teams-field", "size": "5"}
            )
        }


class BaseToDoItemForm(forms.ModelForm):
    class Meta:
        fields = (
            "name",
            "description",
            "deadline",
            "priority",
        )
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                    "class": "form-control",
                }
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Describe the task..."}
            ),
            "priority": forms.Select(
                choices=[
                    (1, "Urgent"),
                    (2, "High"),
                    (3, "Medium"),
                    (4, "Low"),
                    (5, "Optional"),
                ],
                attrs={"class": "form-select", "aria-label": "Select Task Priority"},
            ),
        }
        labels = {"priority": "Select Task Priority"}

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if deadline:
            if deadline < timezone.now() + timezone.timedelta(minutes=15):
                raise ValidationError("Deadline must be at least 15 minutes from now")
        return deadline


class TaskForm(BaseToDoItemForm):
    class Meta(BaseToDoItemForm.Meta):
        model = Task
        fields = (*BaseToDoItemForm.Meta.fields, "task_type", "project", "workers")
        widgets = {
            **BaseToDoItemForm.Meta.widgets,
            "workers": forms.CheckboxSelectMultiple(
                attrs={"class": "form-select workers-field", "size": "5"}
            ),
        }


class TaskWorkersUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("workers",)
        widgets = {
            "workers": forms.CheckboxSelectMultiple(
                attrs={"class": "form-select workers-field", "size": "5"}
            ),
        }


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "search..."}
        ),
    )


class WorkerRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = ("username", "position", "password1", "password2", )
