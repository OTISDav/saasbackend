# Generated by Django 5.1.1 on 2024-10-04 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("videodownloader", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="video",
            options={},
        ),
        migrations.RenameField(
            model_name="video",
            old_name="downloaded_at",
            new_name="uploaded_at",
        ),
        migrations.RemoveField(
            model_name="video",
            name="download_path",
        ),
        migrations.AlterField(
            model_name="video",
            name="url",
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name="video",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]