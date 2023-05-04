from django.contrib import admin

from .models import PatientVisit, Address, Doctor

admin.site.register(PatientVisit)
admin.site.register(Address)
admin.site.register(Doctor)


