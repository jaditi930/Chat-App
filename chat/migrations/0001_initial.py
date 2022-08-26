# Generated by Django 4.1 on 2022-08-20 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=122)),
                ('datetime', models.DateTimeField(blank='True', default=datetime.datetime.now)),
                ('username', models.CharField(max_length=122)),
                ('roomname', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
            ],
        ),
    ]
