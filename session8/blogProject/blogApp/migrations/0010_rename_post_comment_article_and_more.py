# Generated by Django 4.1.7 on 2023-04-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0009_rename_content_recomment_recontent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='recomment',
            old_name='post',
            new_name='comment',
        ),
    ]