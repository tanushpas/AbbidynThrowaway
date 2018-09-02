# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-01 16:23
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsrMgmtModule', '0002_auto_20180901_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(blank=True, default=500000, validators=[django.core.validators.RegexValidator(regex=b'^\\d{6}$')]),
        ),
    ]
