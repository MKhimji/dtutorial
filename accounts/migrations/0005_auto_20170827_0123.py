# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-27 00:23
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        #('home', '0005_friend_current_user'),
        ('admin', '0002_logentry_remove_auto_add'),
        ('accounts', '0004_userimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userimage',
            name='user_ptr',
        ),
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
                ('london', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='UserImage',
        ),
    ]
