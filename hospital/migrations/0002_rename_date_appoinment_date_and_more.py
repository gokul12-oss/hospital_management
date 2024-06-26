# Generated by Django 4.2.11 on 2024-04-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appoinment',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='appoinment',
            old_name='Time',
            new_name='time',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Mobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='Name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
