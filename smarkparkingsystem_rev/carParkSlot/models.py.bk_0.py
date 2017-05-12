#Carpark Slot Info table

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class parkingslot(models.Model):
	parkingslotID           = models.IntegerField(default = 0)
	parkingslotStatus       = models.CharField(max_length=200, default="available")
	parkingslotCode         = models.IntegerField(default = 0)
	
	def __str__(self):
		parkingslotName = "parking slot %d" %(self.parkingslotID)
		return parkingslotName

