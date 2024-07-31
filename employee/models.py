from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
#Table Creation -> Model Creations

# class Employee(models.Model):
#     # Employee Table
#     class StatusChoice(models.TextChoices):
#         ACTIVE = "active", "Active"
#         INACTIVE = "inactive", "Inactive"
    
#     name = models.CharField(max_length=50, null=True, blank=True)
#     status = models.CharField(max_length=10, choices=StatusChoice.choices, default=StatusChoice.ACTIVE)
#     address = models.CharField(max_length=255, null=True, blank=True)
    
class Employee(models.Model):
    #Fields
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    
    