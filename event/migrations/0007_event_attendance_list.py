# Generated by Django 4.2.11 on 2024-03-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_remove_event_event_host_time_ampm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendance_list',
            field=models.TextField(blank=True),
        ),
    ]
