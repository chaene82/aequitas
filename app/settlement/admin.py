from django.contrib import admin
from .models import LegalGuardiant, Patient, Insurance, CostApproval, Settlement, PaymentMethode, Address, CostApprovalType


# Register your models here.
admin.site.register(LegalGuardiant)
admin.site.register(Patient)
admin.site.register(Insurance) 
admin.site.register(CostApproval)
admin.site.register(Settlement)
admin.site.register(PaymentMethode)
admin.site.register(Address)
admin.site.register(CostApprovalType)



