# Generated by Django 4.0.4 on 2022-05-27 19:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('CPL', '0003_userip_cyclingevent_event_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cyclingevent',
            name='event_view',
        ),
        migrations.DeleteModel(
            name='UserIP',
        ),
    ]
