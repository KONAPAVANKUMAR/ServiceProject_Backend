# Generated by Django 4.0.dev20210401123330 on 2021-11-10 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceApp', '0002_service_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='user',
        ),
    ]
