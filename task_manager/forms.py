from django import forms
from django.contrib.auth.forms import UserCreationForm


from task_manager.models import (
    Team,
    Project,
    Worker,
    Task,
)


class WorkerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Worker
        fields = UserCreationForm.Meta.fields + (
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
