from django.contrib import admin
from .models import LegalGuardiant, Patient, Insurance, CostApproval, Settelment, PaymentMethode


# Register your models here.
admin.site.register(LegalGuardiant)
admin.site.register(Patient)
admin.site.register(Insurance) 
admin.site.register(CostApproval)
admin.site.register(Settelment)
admin.site.register(PaymentMethode)

