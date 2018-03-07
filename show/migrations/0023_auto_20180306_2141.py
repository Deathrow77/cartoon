# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 21:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0022_auto_20180306_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='dimension1',
            name='key',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension2',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension3',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension4',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension5',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension6',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension7',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dimension8',
            name='key',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='show.level'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notif',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 3, 6, 21, 39, 56, 558889)),
        ),
    ]
