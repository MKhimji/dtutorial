# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 01:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_blogpost_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='pic',
        ),
    ]
