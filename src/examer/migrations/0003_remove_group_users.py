# Generated by Django 4.1 on 2022-08-04 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examer', '0002_group_users_alter_event_exam_alter_event_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='users',
        ),
    ]
