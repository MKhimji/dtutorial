# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-19 02:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_auto_20180402_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
