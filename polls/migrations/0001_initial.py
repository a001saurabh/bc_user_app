# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10)),
                ('joining_date', models.DateTimeField(verbose_name='date joined')),
                ('name', models.CharField(max_length=40)),
                ('fathers_name', models.CharField(max_length=40)),
                ('classs', models.IntegerField()),
                ('school', models.CharField(max_length=40)),
            ],
        ),
    ]
