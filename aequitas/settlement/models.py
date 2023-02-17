from django.db import models

# Create your models here.
class LegalGuardiant(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    display_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)   
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return self.display_name

class Patient(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    display_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)   
    legalGuardiant = models.ForeignKey(LegalGuardiant,
                     on_delete=models.CASCADE,
                     related_name='Patient_LegalGuardiant',
                     null=True)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.display_name

class PaymentMethode(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    bank = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    IBAN = models.CharField(max_length=100)
    beneficjent = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Insurance(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CostApproval(models.Model):
    name = models.CharField(max_length=250)
    patient = models.ForeignKey(Patient,
                    on_delete=models.CASCADE,
                    related_name='CostApproval_patient')
    insurance = models.ForeignKey(Insurance,
                    on_delete=models.CASCADE,
                    related_name='CostApproval_insurance')         
    paymentMethode = models.ForeignKey(PaymentMethode,
                    on_delete=models.CASCADE,
                    related_name='CostApproval_paymentMethode', null=True)                 
    type = models.CharField(max_length=100)
    refCode = models.CharField(max_length=100)
    templateForm = models.CharField(max_length=100)
    startDate = models.DateField(null=True)
    EndDate = models.DateField(null=True)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name 
        
class Settelment(models.Model):
    name = models.CharField(max_length=250)
    costApproval = models.ForeignKey(CostApproval,
                    on_delete=models.CASCADE,
                    related_name='Settlement_costApproval')             
    status = models.CharField(max_length=100)
    startDate = models.DateField(null=True, blank=True)
    EndDate = models.DateField(null=True, blank=True)
    invoiceDate = models.DateTimeField(null=True, blank=True)
    paymentDate = models.DateTimeField(null=True, blank=True)
    documentPath = models.CharField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name 



