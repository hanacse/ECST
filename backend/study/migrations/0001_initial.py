# Generated by Django 5.0.1 on 2024-02-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=300)),
                ('study_todo', models.CharField(max_length=300)),
                ('study_time', models.TimeField(auto_now_add=True)),
                ('study_completed', models.BooleanField(default=False)),
                ('study_status', models.TimeField(auto_now_add=True)),
                ('study_description', models.CharField(max_length=300)),
            ],
        ),
    ]
