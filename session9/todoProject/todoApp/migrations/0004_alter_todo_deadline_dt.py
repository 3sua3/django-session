# Generated by Django 4.2 on 2023-04-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_remove_todo_updated_dt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_dt',
            field=models.DateField(auto_now=True),
        ),
    ]