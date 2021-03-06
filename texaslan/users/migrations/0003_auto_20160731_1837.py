# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 23:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0002_auto_20160731_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Drew Romanyk', max_length=255, verbose_name='Full Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='graduation_year',
            field=models.DateField(default=datetime.datetime(2016, 7, 31, 23, 37, 40, 904906, tzinfo=utc),
                                   verbose_name='Graduation Year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nick_name',
            field=models.CharField(default='Drew', max_length=255, verbose_name='Nick Name'),
            preserve_default=False,
        ),
    ]
