# Generated by Django 5.0.2 on 2024-02-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NovaBazaar", "0014_order_date_order_user_alter_order_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="address",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]