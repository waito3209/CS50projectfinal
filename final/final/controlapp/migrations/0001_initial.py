# Generated by Django 2.1.7 on 2020-05-28 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customersapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driverapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cardata',
            fields=[
                ('carnumber', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('carname', models.TextField()),
                ('color', models.CharField(blank=True, max_length=10)),
                ('seatnumber', models.SmallIntegerField()),
                ('price_hour', models.SmallIntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Controllstaff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('company', models.CharField(blank=True, max_length=50)),
                ('phonenumber', models.CharField(max_length=11)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmed', models.BooleanField(blank=True, default=False)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField(blank=True, null=True)),
                ('start_place', models.CharField(max_length=100)),
                ('end_place', models.CharField(blank=True, max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlapp.Cardata')),
                ('controllstaff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='controlapp.Controllstaff')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customersapp.Customer')),
                ('driver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='driverapp.Driver')),
            ],
        ),
    ]
