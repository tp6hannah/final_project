# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170603_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='category',
            field=models.CharField(default=111, max_length=10),
            preserve_default=False,
        ),
    ]
