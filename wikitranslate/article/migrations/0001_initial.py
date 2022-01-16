# Generated by Django 3.2.11 on 2022-01-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wiki_title', models.CharField(max_length=200)),
                ('target_lang', models.CharField(choices=[('hi', 'Hindi'), ('bn', 'Bengali'), ('pa', 'Punjabi'), ('te', 'Telugu'), ('ta', 'Tamil')], default='hi', max_length=7)),
            ],
        ),
    ]
