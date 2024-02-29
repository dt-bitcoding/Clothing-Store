# Generated by Django 5.0.2 on 2024-02-29 06:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NovaBazaar", "0009_cart_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total",
        ),
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="city",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]