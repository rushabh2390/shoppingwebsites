# Generated by Django 3.2.4 on 2021-08-23 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_orders_order'),
        ('products', '0002_rename_products_product'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sellers',
            new_name='Seller',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]