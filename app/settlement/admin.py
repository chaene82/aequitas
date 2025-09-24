from django.contrib import admin
from .models import LegalGuardian, Patient, Insurance, CostApproval, Settlement, PaymentMethod, Address, CostApprovalType


# Register your models here.
admin.site.register(LegalGuardian)
admin.site.register(Patient)
admin.site.register(Insurance) 
admin.site.register(CostApproval)
admin.site.register(Settlement)
admin.site.register(PaymentMethod)
admin.site.register(Address)
admin.site.register(CostApprovalType)



