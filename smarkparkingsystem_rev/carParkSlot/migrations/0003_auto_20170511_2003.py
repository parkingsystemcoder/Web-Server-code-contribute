# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carParkSlot', '0002_auto_20170509_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingslot',
            old_name='parkingslotCode',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='parkingslot',
            old_name='parkingslotStatus',
            new_name='status',
        ),
        migrations.RemoveField(
            model_name='parkingslot',
            name='parkingslotID',
        ),
    ]