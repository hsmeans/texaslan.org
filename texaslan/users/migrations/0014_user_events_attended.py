# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-02 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20180721_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events_attended',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
