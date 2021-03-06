# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 05:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='json',
            field=jsonfield.fields.JSONField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='level',
            name='image',
            field=models.FileField(default='images/level12.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 3, 6, 5, 31, 36, 326328)),
        ),
    ]
