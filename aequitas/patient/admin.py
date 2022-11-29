from django.contrib import admin
from .models import Diagnosis, Patient

admin.site.register(Diagnosis)
admin.site.register(Patient)

# Register your models here.
