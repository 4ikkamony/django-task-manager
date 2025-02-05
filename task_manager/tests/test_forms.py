from django.test import TestCase

from django.utils import timezone

from task_manager.forms import TaskForm
from task_manager.models import TaskType


class TaskFormTest(TestCase):
    def setUp(self):
        self.task_type = TaskType.objects.create(name="Test Task Type")
        self.form_data = {
            "name": "Test task",
            "description": "Test description",
            "task_type": self.task_type.id,
            "priority": 3,
        }

    def test_clean_deadline_16_minutes_from_now_valid(self):
        future_deadline = timezone.now() + timezone.timedelta(minutes=16)

        self.form_data["deadline"] = future_deadline

        form = TaskForm(data=self.form_data)

        self.assertTrue(form.is_valid())

    def test_clean_deadline_15_minutes_from_now_invalid(self):
        past_deadline = timezone.now() + timezone.timedelta(minutes=15)

        self.form_data["deadline"] = past_deadline

        form = TaskForm(data=self.form_data)

        self.assertFalse(form.is_valid())

    def test_clean_deadline_not_specified(self):
        form = TaskForm(data=self.form_data)

        self.assertTrue(form.is_valid())
