# Generated by Django 5.0.2 on 2024-09-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_article_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='news_of_the_day',
            field=models.BooleanField(default=False, verbose_name='Chop etish'),
        ),
    ]