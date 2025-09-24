from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)   
    
    def __str__(self):
        parts = [
            self.address or '',
            f"{self.zip_code or ''} {self.city or ''}".strip()
        ]
        return ', '.join(filter(None, parts)) or 'No Address'   


class LegalGuardian(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    display_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='legal_guardian_address',
                     null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.display_name

class Patient(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    display_name = models.CharField(max_length=100)
    social_insurance_number = models.CharField(max_length=20, null=True) 
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='patient_address',
                     null=True) 
    legal_guardian = models.ForeignKey(LegalGuardian,
                     on_delete=models.CASCADE,
                     related_name='patient_legal_guardian',
                     null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=250)
    pm_type = models.CharField(max_length=250)
    bank = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    IBAN = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Insurance(models.Model):
    name = models.CharField(max_length=250)
    insurance_type = models.CharField(max_length=250)
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='insurance_address',
                     null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CostApprovalType(models.Model):
    name = models.CharField(max_length=250)
    template_form = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CostApproval(models.Model):
    name = models.CharField(max_length=250)
    patient = models.ForeignKey(Patient,
                    on_delete=models.CASCADE,
                    related_name='cost_approval_patient')
    insurance = models.ForeignKey(Insurance,
                    on_delete=models.CASCADE,
                    related_name='cost_approval_insurance')         
    payment_method = models.ForeignKey(PaymentMethod,
                    on_delete=models.CASCADE,
                    related_name='cost_approval_payment_method', null=True)                 
    ref_code = models.CharField(max_length=100)
    ca_type = models.ForeignKey(CostApprovalType,
                    on_delete=models.CASCADE,
                    related_name='cost_approval_type', null=True)  
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    amount = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name 
        
class Settlement(models.Model):
    name = models.CharField(max_length=250)
    cost_approval = models.ForeignKey(CostApproval,
                    on_delete=models.CASCADE,
                    related_name='settlement_cost_approval')             
    status = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    requested_amount = models.FloatField(null=True)
    received_amount = models.FloatField(null=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    document_path = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name 
    


