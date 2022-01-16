# Generated by Django 3.2.11 on 2022-01-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_sentence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='sentence_id',
        ),
        migrations.AddField(
            model_name='sentence',
            name='original_sentence',
            field=models.TextField(default='NA'),
        ),
        migrations.AddField(
            model_name='sentence',
            name='translated_sentence',
            field=models.TextField(blank=True),
        ),
    ]