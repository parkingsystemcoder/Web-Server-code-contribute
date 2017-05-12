#User Info table

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	username        = models.CharField(max_length=200, default="NA")
	password        = models.CharField(max_length=200, default="NA")
	paystatus       = models.IntegerField(default=0)
	code            = models.IntegerField(default=0)
	def __str__(self):
		userName = "user ID %d" %(self.id)
		return userName
