# Generated by Django 3.2.4 on 2021-08-31 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productTax',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
