# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 13:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OJ', '0003_auto_20160429_2051'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Discuss',
        ),
        migrations.RenameField(
            model_name='discuss',
            old_name='comments',
            new_name='discuss',
        ),
    ]
