# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carParkSlot', '0003_auto_20170511_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingslot',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
