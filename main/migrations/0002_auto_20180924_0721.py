# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-24 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='order',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]