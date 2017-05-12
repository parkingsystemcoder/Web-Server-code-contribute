#User Info table

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	userID                  = models.IntegerField(default = 0)
	userName                = models.CharField(max_length=200, default="NA")
	userPassword            = models.CharField(max_length=200, default="NA")
	userPaymentStatus       = models.IntegerField(default=0)
	userCode                = models.IntegerField(default=0)
	def __str__(self):
		userName = "user ID %d" %(self.userID)
		return userName
