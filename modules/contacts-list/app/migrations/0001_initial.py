# Generated by Django 4.2.6 on 2023-12-01 15:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField()),
                ("email", models.TextField()),
                ("phone", models.TextField()),
                ("is_favorite", models.BooleanField()),
            ],
        ),
    ]
