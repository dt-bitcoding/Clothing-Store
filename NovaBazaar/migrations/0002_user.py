# Generated by Django 5.0.1 on 2024-02-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NovaBazaar", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("FirstName", models.CharField(max_length=100)),
                ("Email", models.EmailField(max_length=100)),
                ("Password", models.CharField(max_length=100)),
                ("confirm_password", models.CharField(max_length=100)),
            ],
        ),
    ]
