# Generated by Django 4.2 on 2023-07-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kb_statistics', '0006_alter_session_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.TextField(default=' ', null=True),
        ),
    ]
