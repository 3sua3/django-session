# Generated by Django 4.1.7 on 2023-04-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_article_category_article_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=30),
        ),
    ]
