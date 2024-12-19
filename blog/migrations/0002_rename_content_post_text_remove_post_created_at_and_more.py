# Generated by Django 5.1.4 on 2024-12-19 07:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="content",
            new_name="text",
        ),
        migrations.RemoveField(
            model_name="post",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
        migrations.AddField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]