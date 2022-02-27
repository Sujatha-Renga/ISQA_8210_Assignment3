from django.contrib import admin

from .models import BloodStock, BloodRequest

admin.site.register(BloodRequest)
admin.site.register(BloodStock)
