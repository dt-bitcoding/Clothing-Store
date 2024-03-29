# Generated by Django 5.0.2 on 2024-02-26 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("NovaBazaar", "0003_alter_cart_quantity_alter_product_product_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="quantity",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="user",
        ),
        migrations.AddField(
            model_name="cart",
            name="discription",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cart",
            name="name",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cart",
            name="price",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="product_image",
            field=models.ImageField(upload_to="Product/"),
        ),
    ]
