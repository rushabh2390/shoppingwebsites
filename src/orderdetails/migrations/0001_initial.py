# Generated by Django 3.2.4 on 2021-08-22 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('orderDetailsID', models.BigAutoField(primary_key=True, serialize=False)),
                ('orderDetailsProductPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('orderDetailsDiscount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oredrDetailsOrderQty', models.DecimalField(decimal_places=2, max_digits=5)),
                ('orderDetailsProductID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
                ('orderDetailsorderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
            ],
        ),
    ]
