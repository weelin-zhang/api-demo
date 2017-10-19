# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('description', models.TextField(verbose_name='\u63cf\u8ff0')),
                ('completed', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5b8c\u6210')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
    ]
