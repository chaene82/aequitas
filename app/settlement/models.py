from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)   
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        ordering = ['city', 'zip_code']
    
    def __str__(self):
        parts = [
            self.address or '',
            f"{self.zip_code or ''} {self.city or ''}".strip()
        ]
        return ', '.join(filter(None, parts)) or 'No Address'   


class LegalGuardian(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    display_name = models.CharField(max_length=100)
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='legal_guardian_address',
                     null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    class Meta:
        verbose_name = "Legal Guardian"
        verbose_name_plural = "Legal Guardians"
        ordering = ['display_name']

    def __str__(self):
        return self.display_name

class Patient(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250, null=True, blank=True)
    display_name = models.CharField(max_length=100)
    social_insurance_number = models.CharField(max_length=20, null=True, blank=True) 
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='patient_address',
                     null=True, blank=True) 
    legal_guardian = models.ForeignKey(LegalGuardian,
                     on_delete=models.CASCADE,
                     related_name='patient_legal_guardian',
                     null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
        ordering = ['display_name']

    def __str__(self):
        return self.display_name

class PaymentMethod(models.Model):
    """Model representing payment methods for transactions."""
    name = models.CharField(max_length=250)
    pm_type = models.CharField(max_length=250)
    bank = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    IBAN = models.CharField(max_length=100)
    beneficiary = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Payment Method"
        verbose_name_plural = "Payment Methods"
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Insurance(models.Model):
    """Model representing insurance companies and policies."""
    name = models.CharField(max_length=250)
    insurance_type = models.CharField(max_length=250, verbose_name="Insurance Type")
    address = models.ForeignKey(Address,
                     on_delete=models.CASCADE,
                     related_name='insurance_address',
                     null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Insurance"
        verbose_name_plural = "Insurances"
        ordering = ['name']

    def __str__(self):
        return self.name

class CostApprovalType(models.Model):
    """Model representing different types of cost approvals."""
    name = models.CharField(max_length=250)
    template_form = models.CharField(max_length=100, verbose_name="Template Form")
    
    class Meta:
        verbose_name = "Cost Approval Type"
        verbose_name_plural = "Cost Approval Types"
        ordering = ['name']
    
    def __str__(self):
        return self.name

class CostApproval(models.Model):
    """Model representing cost approvals for patient treatments."""
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
    ref_code = models.CharField(max_length=100, verbose_name="Reference Code")
    ca_type = models.ForeignKey(CostApprovalType,
                    on_delete=models.CASCADE,
                    related_name='cost_approval_type', null=True, blank=True)  
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cost Approval"
        verbose_name_plural = "Cost Approvals"
        ordering = ['-created']

    def __str__(self):
        return self.name 
        
class Settlement(models.Model):
    """Model representing settlements and payments."""
    name = models.CharField(max_length=250)
    cost_approval = models.ForeignKey(CostApproval,
                    on_delete=models.CASCADE,
                    related_name='settlement_cost_approval')             
    status = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    requested_amount = models.FloatField(null=True, blank=True)
    received_amount = models.FloatField(null=True, blank=True)
    invoice_date = models.DateTimeField(null=True, blank=True)
    payment_date = models.DateTimeField(null=True, blank=True)
    document_path = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Settlement"
        verbose_name_plural = "Settlements"
        ordering = ['-created']

    def __str__(self):
        return self.name 
    


