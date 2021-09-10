# Generated by Django 3.2.4 on 2021-08-22 17:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('userFirstName', models.CharField(max_length=200)),
                ('userLastName', models.CharField(max_length=200)),
                ('userEmail', models.EmailField(max_length=300)),
                ('userPwd', models.CharField(max_length=200)),
                ('userAddress', models.TextField(max_length=300)),
                ('userShipmentAddress', models.TextField(max_length=300)),
                ('userContactNo', models.CharField(blank=True, max_length=60, null=True, validators=[django.core.validators.RegexValidator(message='Please enter 10 digits mobiel number', regex='^\\d{10}$')])),
                ('isSeller', models.BooleanField(default=False)),
                ('profilephoto', models.ImageField(blank=True, null=True, upload_to='profile/')),
            ],
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=200)),
                ('companyGSTIN', models.CharField(max_length=200)),
                ('panNumber', models.CharField(max_length=10)),
                ('registeredAddress', models.CharField(max_length=300)),
                ('pickupAddress', models.CharField(max_length=300)),
                ('aadharCopy', models.ImageField(blank=True, null=True, upload_to='aadhar/')),
                ('gstincertificate', models.ImageField(blank=True, null=True, upload_to='GSTIN/')),
                ('panCopy', models.ImageField(blank=True, null=True, upload_to='pancard/')),
                ('bankAccountNumber', models.IntegerField()),
                ('bankIFSCCode', models.CharField(max_length=20)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
