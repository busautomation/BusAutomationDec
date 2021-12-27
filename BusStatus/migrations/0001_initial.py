# Generated by Django 4.0 on 2021-12-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusSatusData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BusNo', models.CharField(max_length=10)),
                ('DriverName', models.CharField(max_length=50)),
                ('ConductorName', models.CharField(max_length=50)),
                ('DepartureTime', models.CharField(max_length=50)),
                ('ArrivalTime', models.CharField(max_length=50)),
                ('LastService', models.CharField(max_length=50)),
                ('PUC', models.DateTimeField()),
                ('Insurance', models.DateTimeField()),
                ('DriverContactNo', models.CharField(max_length=50)),
                ('ConductorContactNo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FuelDataPercentage', models.FloatField()),
                ('FuelDataLitre', models.FloatField()),
                ('Temperature', models.FloatField()),
                ('Humidity', models.FloatField()),
                ('FireHydrantPercentage', models.FloatField()),
                ('FireHydrantKg', models.FloatField()),
            ],
        ),
    ]