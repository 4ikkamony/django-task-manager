# Generated by Django 5.1.5 on 2025-02-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task_manager", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="project",
            name="tags",
        ),
        migrations.AddField(
            model_name="project",
            name="priority",
            field=models.IntegerField(
                default=3,
                verbose_name=[
                    (1, "Urgent"),
                    (2, "High"),
                    (3, "Medium"),
                    (4, "Low"),
                    (5, "Optional"),
                ],
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                default=3,
                verbose_name=[
                    (1, "Urgent"),
                    (2, "High"),
                    (3, "Medium"),
                    (4, "Low"),
                    (5, "Optional"),
                ],
            ),
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
