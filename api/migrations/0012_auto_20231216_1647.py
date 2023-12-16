# Generated by Django 3.2.23 on 2023-12-16 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_profile_education'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.ManyToManyField(to='api.Education'),
        ),
        migrations.RemoveField(
            model_name='profile',
            name='experience',
        ),
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.ManyToManyField(to='api.Experience'),
        ),
    ]