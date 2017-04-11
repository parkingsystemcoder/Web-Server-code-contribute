from django.contrib import admin

# Register your models here.
from .models import driver_detail

admin.site.register(driver_detail)

#class websystem_admin(admin.ModelAdmin):
   # fieldsets = [('Driver_Information', {'fields':['driver_name','driver_ID']}),
                # ('Car_Information',{'fields':['car_number','car_color']}),]


