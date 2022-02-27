from django.contrib import admin
from .models import BloodDonate, Donar


class DonarAdmin(admin.ModelAdmin):
    list_display = ('Donar_name', 'gender', 'age', 'blood_group', 'email', 'mobile', 'address')


admin.site.register(Donar, DonarAdmin)


class BloodDonateAdmin(admin.ModelAdmin):
    list_display = ('donor', 'disease', 'age', 'bloodgroup', 'unit', 'status', 'date')


admin.site.register(BloodDonate, BloodDonateAdmin)
