from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    salary = models.FloatField(blank=True,null=True)
    designation = models.CharField(max_length=255,blank=True,null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,blank=True,null=True)
    address = models.CharField(max_length=255,blank=True,null=True)
    projects = models.ManyToManyField('Project',blank=True,null=True,related_name='employees')

    def __str__(self):
        return self.name

class Project(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('ON-GOING', 'On-Going'),
        ('ENDED', 'Ended'),
    ]

    name = models.CharField(max_length=255,blank=True,null=True)
    team = models.ManyToManyField(Employee, related_name='project_team',blank=True,null=True)
    team_lead = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='team_lead',blank=True,null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,blank=True,null=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name
