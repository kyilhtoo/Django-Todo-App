# Generated by Django 3.0.5 on 2020-04-26 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_name',
            field=models.TextField(max_length=300),
        ),
    ]