# Generated by Django 4.1.7 on 2023-04-12 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0007_comment_recomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recomments', to='blogApp.comment'),
        ),
    ]
