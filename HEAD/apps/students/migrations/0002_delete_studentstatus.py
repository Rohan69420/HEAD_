# Generated by Django 4.2.3 on 2023-08-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='studentStatus',
        ),
    ]