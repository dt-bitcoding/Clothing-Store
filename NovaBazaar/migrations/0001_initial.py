# Generated by Django 5.0.1 on 2024-02-06 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("ProductName", models.CharField(max_length=100)),
                ("Category", models.CharField(max_length=100)),
                ("Order", models.IntegerField()),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
