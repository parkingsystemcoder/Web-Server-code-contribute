#Carpark Slot Info table

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class parkingslot(models.Model):
	status       = models.IntegerField(default = 1)
	code         = models.IntegerField(default = 0)
	
	def __str__(self):
		parkingslotName = "parking slot %d" %(self.id)
		return parkingslotName

