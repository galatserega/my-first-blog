# Generated by Django 5.1.4 on 2024-12-19 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_rename_content_post_text_remove_post_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
