# Generated by Django 4.0.4 on 2022-05-25 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EventParticipatingGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPL.user')),
            ],
        ),
        migrations.CreateModel(
            name='CyclingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.TextField()),
                ('event_description', models.TextField()),
                ('distance', models.TextField()),
                ('prize_pool', models.FloatField()),
                ('event_date', models.DateField()),
                ('participating_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CPL.eventparticipatinggroup')),
            ],
        ),
    ]
