# Generated by Django 4.2.11 on 2024-04-01 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(max_length=50)),
                ('special', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=10)),
                ('Mobile', models.IntegerField(null=True)),
                ('Address', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.doctor')),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.patient')),
            ],
        ),
    ]
