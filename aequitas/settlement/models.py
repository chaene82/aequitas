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

    def __unicode__(self):
        return u'%s' % (self.display_name)

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

    def __unicode__(self):
        return u'%s' % (self.display_name)

class Insurance(models.Model):
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return u'%s' % (self.name)

# class CostApproval(models.Model):
#     name = models.CharField(max_length=250)
#     patient = models.ForeignKey(Patient,
#                     on_delete=models.CASCADE,
#                     related_name='CostApproval_patient')
#     insurance = models.ForeignKey(Insurance,
#                     on_delete=models.CASCADE,
#                     related_name='CostApproval_insurance')                    
#     type = models.CharField(max_length=100)
#     refCode = models.CharField(max_length=100)

