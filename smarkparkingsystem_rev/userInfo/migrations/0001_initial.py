# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField(default=0)),
                ('userPaymentStatus', models.CharField(default='available', max_length=200)),
                ('userCode', models.IntegerField(default=0)),
            ],
        ),
    ]
