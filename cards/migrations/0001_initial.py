# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-16 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('photo_url', models.URLField()),
                ('planet', models.CharField(max_length=30)),
            ],
        ),
    ]
