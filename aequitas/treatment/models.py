from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# class Institute(models.Model):
#     title = models.CharField(max_length=250)
#     address = models.CharField(max_length=250)
#     def __str__(self):
#         return self.title


class Institute(models.Model):
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    def __str__(self):
        return self.title



    



