# Generated by Django 3.2.9 on 2021-11-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('LaptopId', models.AutoField(primary_key=True, serialize=False)),
                ('LaptopName', models.CharField(max_length=500)),
                ('LaptopImage', models.CharField(max_length=5000)),
                ('LaptopScreenSize', models.FloatField()),
                ('LaptopScreenResolution', models.FloatField()),
                ('LaptopRam', models.FloatField()),
                ('LaptopHDD', models.FloatField()),
                ('LaptopSSD', models.FloatField()),
                ('LaptopDetails', models.CharField(max_length=1000)),
                ('LaptopPrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('MobileId', models.AutoField(primary_key=True, serialize=False)),
                ('MobileName', models.CharField(max_length=500)),
                ('MobileImage', models.CharField(max_length=5000)),
                ('MobileRom', models.CharField(max_length=500)),
                ('MobileScreen', models.FloatField()),
                ('MobilePrimaryCam', models.FloatField()),
                ('MobileSalfieCam', models.FloatField()),
                ('MobileBattery', models.FloatField()),
                ('MobileDetails', models.CharField(max_length=1000)),
                ('MobilePrice', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserEmail', models.CharField(max_length=500)),
                ('UserFirstName', models.CharField(max_length=500)),
                ('UserLastName', models.CharField(max_length=500)),
                ('UserContactNo', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserEmail', models.CharField(max_length=500)),
                ('UserPassword', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('UserFirstName', models.CharField(max_length=500)),
                ('UserLastName', models.CharField(max_length=500)),
                ('UserContactNo', models.CharField(max_length=500)),
                ('UserEmail', models.CharField(max_length=500)),
                ('UserPassword', models.CharField(max_length=500)),
            ],
        ),
    ]