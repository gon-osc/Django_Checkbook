# Generated by Django 3.1 on 2020-08-24 17:28

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0005_auto_20200821_1818'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('Account', django.db.models.manager.Manager()),
            ],
        ),
    ]
