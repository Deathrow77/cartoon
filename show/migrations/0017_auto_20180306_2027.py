# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0016_auto_20180306_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 3, 6, 20, 27, 41, 154358)),
        ),
    ]
