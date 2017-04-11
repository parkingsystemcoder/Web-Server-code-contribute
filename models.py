from __future__ import unicode_literals
from django.db import models

# Create your models here.

class driver_detail(models.Model):
    driver_name = models.CharField(max_length=30)
    driver_ID = models.CharField(max_length=30)
    car_number = models.CharField(max_length=10)
    car_color = models.CharField(max_length=10)
    #time_check_in = models.DateTimeField(auto_now_add=True)
    #time_check_out = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.driver_name