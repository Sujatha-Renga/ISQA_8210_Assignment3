from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('Patient', 'age', 'bloodgroup', 'disease', 'doctorname', 'email', 'address', 'mobile')


admin.site.register(Patient, PatientAdmin)
