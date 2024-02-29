# Generated by Django 5.0.2 on 2024-02-29 06:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NovaBazaar", "0011_remove_order_user_order_customer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="city",
            new_name="phone",
        ),
        migrations.RemoveField(
            model_name="order",
            name="name",
        ),
        migrations.AddField(
            model_name="order",
            name="date",
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
