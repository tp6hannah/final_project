# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
