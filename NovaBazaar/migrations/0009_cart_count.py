# Generated by Django 5.0.2 on 2024-02-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "NovaBazaar",
            "0008_remove_cart_product_image_remove_cart_selling_price_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="count",
            field=models.IntegerField(default=1),
        ),
    ]
