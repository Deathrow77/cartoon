# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 13:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0004_auto_20180306_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 3, 6, 13, 31, 8, 827138)),
        ),
    ]
