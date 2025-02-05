from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import (
    Position,
    Task,
    TaskType
)


Worker = get_user_model()


POSITION_URL = reverse("task_manager:position-list")


class PositionTest(TestCase):
    def setUp(self) -> None:
        self.worker = Worker.objects.create_user(
            username="testuser",
            password="test1test23",
        )
        self.client.login(self.worker)

    def test_retrieve_position(self):
        Position.objects.create(name="testposition1")
        Position.objects.create(name="testposition2")
        res = self.client.get(POSITION_URL)
        self.assertEqual(res.status_code, 200)
        positions = Position.objects.all()
        self.assertEqual(
            list(res.context["position_list"]),
            list(positions),
        )
        self.assertTemplateUsed(
            res,
            "task_manager/position_list.html"
        )


class ToggleTaskToStatusTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.worker = Worker.objects.create_user(
            username="testworker",
            password="password123",
        )
        cls.task_type = TaskType.objects.create(
            name="test type",
        )
        cls.task = Task.objects.create(
            name="Test Task",
            description="Some task",
            task_type=cls.task_type,
        )

    def test_toggle_task_status(self):
        self.client.login(username="testworker", password="password123")

        self.assertFalse(self.task.is_completed)

        response = self.client.post(
            reverse(
                "task_manager:task-toggle-status",
                args=[self.task.pk]
            )
        )
        self.assertRedirects(
            response,
            reverse("task_manager:task-list")
        )

        self.task.refresh_from_db()

        self.assertTrue(self.task.is_completed)

        response = self.client.post(
            reverse(
                "task_manager:task-toggle-status",
                args=[self.task.pk])
        )
        self.assertRedirects(
            response,
            reverse("task_manager:task-list")
        )

        self.task.refresh_from_db()

        self.assertFalse(self.task.is_completed)
