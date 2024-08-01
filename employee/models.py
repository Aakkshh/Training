from django.db import models
from datetime import datetime
class Department(models.Model):
    name = models.CharField(max_length=30) 
    location = models.CharField(max_length=30)

# id Primary key 1
#name Frontend 
#location Texas

class Position(models.Model):
    #id 1
    #role Senior Frontend Developer
    role=models.CharField(max_length=50)
    
class Employee(models.Model):
    #id 1
    first_name=models.CharField(max_length=50, null =True ,blank=True) #Aaakarshak
    last_name=models.CharField(max_length=50, null =True ,blank=True)#Shotri
    email=models.EmailField(max_length=50, null =True ,blank=True)#email
    phone_number=models.CharField(max_length=10,null=True,blank=True)
    
    #TODO: JSON body request for dob and hire_date
    date_of_birth=models.DateField(max_length=20,null=True, blank=True)
    hire_date=models.DateField(max_length=20, null=True, blank=True)
    salary=models.DecimalField(max_digits=30, decimal_places=3, blank= True, null = True)
    #Foreign Keys
    department=models.ForeignKey(Department,on_delete=models.CASCADE ,null=True) #1
    position=models.ForeignKey(Position,on_delete=models.CASCADE, null= True) #1
    
    #One to One Field
    
    #one to many
    
    #many to one
    
    #many to many