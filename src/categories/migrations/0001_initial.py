# Generated by Django 3.2.4 on 2021-08-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoryID', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=200)),
                ('categoryDesc', models.CharField(max_length=300)),
            ],
        ),
    ]
