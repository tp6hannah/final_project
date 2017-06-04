# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_choice_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_name', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=0, max_digits=3)),
                ('comment', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Store'),
        ),
    ]
