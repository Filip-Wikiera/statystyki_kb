# Generated by Django 4.2 on 2023-07-20 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kb_statistics', '0002_session_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='duration',
        ),
    ]
