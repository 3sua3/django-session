# Generated by Django 4.2 on 2023-04-10 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0002_rename_post_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='updated_dt',
        ),
    ]