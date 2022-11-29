from django.db import models

# Create your models here.

class Diagnosis(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250)


class Patient(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    display_name = models.CharField(max_length=100)
    diagnosis = models.ForeignKey(Diagnosis,
                    on_delete=models.CASCADE,
                    related_name='patient_diagnosis')
    create = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)






