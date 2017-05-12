#Server System Info

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class systemInfo(models.Model):
	userID                  = models.IntegerField(default = 0)
	userPaymentStatus       = models.CharField(max_length=200, default="NA")
	userCode                = models.CharField(max_length=200, default="NA")

	parkingslotID           = models.CharField(max_length=200, default="NA")
	parkingslotStatus       = models.CharField(max_length=200, default="NA")
	parkingslotCode         = models.CharField(max_length=200, default="NA")
	
	def __str__(self):
		systemInfoName = "System Information of User %d" %(self.userID)
		return systemInfoName
