# Generated by Django 5.0 on 2023-12-08 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_site', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
    ]
