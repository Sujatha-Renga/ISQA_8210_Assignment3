from django.contrib import admin

from .models import BloodStock, BloodRequest


class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ('request_by_patient', 'request_by_donor', 'patient_name', 'patient_age', 'reason', 'bloodgroup', 'unit', 'status', 'date')
    list_filter = ['patient_name', 'bloodgroup']


admin.site.register(BloodRequest, BloodRequestAdmin)


class BloodStockAdmin(admin.ModelAdmin):
    list_display = ('blood_group', 'units')
    list_filter = ['blood_group', 'units']


admin.site.register(BloodStock, BloodStockAdmin)
