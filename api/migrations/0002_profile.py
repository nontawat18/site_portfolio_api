# Generated by Django 3.2.23 on 2023-12-14 09:12

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('fullname', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.IntegerField()),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=api.models.upload_to)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
    ]
