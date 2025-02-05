from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from task_manager.models import Position, Task, TaskType


Worker = get_user_model()


class LoggedInTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = Worker.objects.create_user(
            username="logged_in_testworker", password="password123"
        )

    def setUp(self):
        self.client.login(username="logged_in_testworker", password="password123")


class IndexViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:index"))
        self.assertEqual(response.status_code, 200)


class TaskTypeListViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/task-types/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:task-type-list"))
        self.assertEqual(response.status_code, 200)


class TaskTypeCreateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/task-types/create/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:task-type-create"))
        self.assertEqual(response.status_code, 200)


class TaskTypeUpdateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        task_type = TaskType.objects.create(name="Test TaskType")
        response = self.client.get(f"/task-types/{task_type.pk}/update/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        task_type = TaskType.objects.create(name="Test TaskType")
        response = self.client.get(
            reverse("task_manager:task-type-update", kwargs={"pk": task_type.pk})
        )
        self.assertEqual(response.status_code, 200)


class TaskTypeDeleteViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        task_type = TaskType.objects.create(name="Test TaskType")
        response = self.client.get(f"/task-types/{task_type.pk}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        task_type = TaskType.objects.create(name="Test TaskType")
        response = self.client.get(
            reverse("task_manager:task-type-delete", kwargs={"pk": task_type.pk})
        )
        self.assertEqual(response.status_code, 200)


class PositionListViewTest(LoggedInTestCase):
    def setUp(self) -> None:
        super().setUp()
        self.position1 = Position.objects.create(name="First")
        self.position2 = Position.objects.create(name="iSecond")
        self.position3 = Position.objects.create(name="Third")

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/positions/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:position-list"))
        self.assertEqual(response.status_code, 200)

    def test_search_no_match(self):
        response = self.client.get(
            reverse("task_manager:position-list"),
            {"query": "NO MATCH"},
        )
        for pos in (self.position1, self.position2, self.position3):
            self.assertNotContains(response, pos.name)

    def test_search_all_match(self):
        response = self.client.get(
            reverse("task_manager:position-list"),
            {"query": "i"},
        )
        for pos in (self.position1, self.position2, self.position3):
            self.assertContains(response, pos.name)

    def test_search_one_match(self):
        response = self.client.get(
            reverse("task_manager:position-list"),
            {"query": "First"},
        )

        self.assertContains(response, self.position1.name)

        for pos in (self.position2, self.position3):
            self.assertNotContains(response, pos.name)


class PositionCreateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/positions/create/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:position-create"))
        self.assertEqual(response.status_code, 200)


class PositionUpdateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        position = Position.objects.create(name="Test Position")
        response = self.client.get(f"/positions/{position.pk}/update")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        position = Position.objects.create(name="Test Position")
        response = self.client.get(
            reverse("task_manager:position-update", kwargs={"pk": position.pk})
        )
        self.assertEqual(response.status_code, 200)


class PositionDeleteViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        position = Position.objects.create(name="Test Position")
        response = self.client.get(f"/positions/{position.pk}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        position = Position.objects.create(name="Test Position")
        response = self.client.get(
            reverse("task_manager:position-delete", kwargs={"pk": position.pk})
        )
        self.assertEqual(response.status_code, 200)


class WorkerListViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/workers/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:worker-list"))
        self.assertEqual(response.status_code, 200)


class WorkerCreateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/workers/create/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:worker-create"))
        self.assertEqual(response.status_code, 200)


class WorkerDetailViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(f"/workers/{worker.pk}/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(
            reverse("task_manager:worker-detail", kwargs={"pk": worker.pk})
        )
        self.assertEqual(response.status_code, 200)


class WorkerUpdateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(f"/workers/{worker.pk}/update/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(
            reverse("task_manager:worker-update", kwargs={"pk": worker.pk})
        )
        self.assertEqual(response.status_code, 200)


class WorkerDeleteViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(f"/workers/{worker.pk}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        worker = Worker.objects.create(username="testworker")
        response = self.client.get(
            reverse("task_manager:worker-delete", kwargs={"pk": worker.pk})
        )
        self.assertEqual(response.status_code, 200)


class TaskListViewTest(LoggedInTestCase):
    def setUp(self):
        super().setUp()

        self.task_type = TaskType.objects.create(
            name="test type",
        )

        number_of_tasks = 8

        for task_id in range(number_of_tasks):
            Task.objects.create(
                name=f"{task_id} Task for testing purposes",
                description=f"{task_id} Task for testing purposes",
                is_completed=True if task_id % 2 == 0 else False,
                task_type=self.task_type,
            )

    def test_must_be_ordered_by_is_completed_asc_and_created_at_desc(self):
        response = self.client.get(reverse("task_manager:task-list"))

        task_context = response.context["task_list"]
        task_list = Task.objects.all().order_by("is_completed", "-created_at")

        self.assertEqual(
            list(task_context),
            list(task_list[: len(task_context)]),
        )

    def test_must_be_paginated(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue("is_paginated" in response.context)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/tasks/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.assertEqual(response.status_code, 200)


class TaskCreateViewTest(LoggedInTestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/tasks/create/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("task_manager:task-create"))
        self.assertEqual(response.status_code, 200)


class ToggleTaskToStatusViewTests(LoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.task_type = TaskType.objects.create(
            name="test type",
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Some task",
            task_type=self.task_type,
        )

    def test_toggle_task_status(self):
        self.assertFalse(self.task.is_completed)

        response = self.client.post(
            reverse("task_manager:task-toggle-status", args=[self.task.pk])
        )
        self.assertRedirects(response, reverse("task_manager:task-list"))

        self.task.refresh_from_db()

        self.assertTrue(self.task.is_completed)

        response = self.client.post(
            reverse("task_manager:task-toggle-status", args=[self.task.pk])
        )
        self.assertRedirects(response, reverse("task_manager:task-list"))

        self.task.refresh_from_db()

        self.assertFalse(self.task.is_completed)


class TaskUpdateViewTest(LoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.task_type = TaskType.objects.create(name="Test type")

        self.task = Task.objects.create(
            name="Test Task",
            description="Intitial task description",
            deadline=timezone.now() + timezone.timedelta(days=1),
            task_type=self.task_type,
        )
        self.initial_deadline = self.task.deadline

    def test_update_task_valid_data(self):
        response = self.client.post(
            reverse("task_manager:task-update", kwargs={"pk": self.task.id}),
            {
                "name": "New name",
                "description": "New task description",
                "task_type": self.task_type.id,
                "priority": 1,
            },
        )

        self.task.refresh_from_db()

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            Task.objects.get(id=self.task.id).description, "New task description"
        )

    def test_update_task_invalid_deadline(self):
        response = self.client.post(
            reverse("task_manager:task-update", kwargs={"pk": self.task.id}),
            {
                "name": "New task name",
                "description": "New task description",
                "deadline": self.initial_deadline - timezone.timedelta(days=5),
                "task_type": self.task_type.id,
            },
        )

        self.assertEqual(response.status_code, 200)

        Task.objects.get(id=self.task.id).refresh_from_db()

        self.assertEqual(
            Task.objects.get(id=self.task.id).deadline, self.initial_deadline
        )


class TaskDeleteViewTest(LoggedInTestCase):
    def setUp(self):
        super().setUp()
        self.task_type = TaskType.objects.create(name="Test type")

        self.task = Task.objects.create(
            name="Task name",
            description="Task description",
            task_type=self.task_type,
        )

    def test_delete_task(self):
        response = self.client.post(
            reverse(
                "task_manager:task-delete",
                kwargs={"pk": self.task.id},
            ),
        )

        self.assertEqual(response.status_code, 302)

        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
