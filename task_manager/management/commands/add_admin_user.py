import os

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.management.base import BaseCommand
from django.conf import settings

from task_manager.models import Position


class Command(BaseCommand):
    help = "Set random prices for existing movies"

    def handle(self, *args, **kwargs):
        User: type[AbstractUser] = get_user_model()
        new_user_username = os.getenv("ADMIN_USERNAME", "user")
        new_user_email = os.getenv("ADMIN_EMAIL", "user@sample.com")
        new_user_password = os.getenv("ADMIN_PASSWORD", "user1234")
        position = os.getenv("POSITION", "CEO")

        user = User.objects.filter(username=new_user_username).first()

        if user:
            self.stdout.write(
                self.style.SUCCESS(f"User {new_user_username} already exists.")
            )
        else:
            position_instance, _ = Position.objects.get_or_create(name=position)
            user = User(
                username=new_user_username,
                email=new_user_email,
                is_staff=True,
                is_superuser=True,
                position=position_instance,
            )
            user.set_password(new_user_password)
            user.save()

            self.stdout.write(
                    self.style.SUCCESS(f"User {new_user_username} created.")
                )
