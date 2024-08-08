from rest_framework import serializers
from .models import Employee, Department, Project

class CreateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'designation', 'department', 'address', 'projects']

class MinimalEmployeeSerializer(serializers.ModelSerializer):
    department = serializers.StringRelatedField()
    class Meta:
        model = Employee
        fields = ['id', 'name', 'designation','department','salary']

class DetailEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'salary', 'designation', 'department', 'address', 'projects']

class UpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'salary', 'designation', 'department', 'address', 'projects']

class ProjectSerializer(serializers.ModelSerializer):
    #team = DetailEmployeeSerializer(many=True, read_only=True)
    #team_lead = DetailEmployeeSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    employees = DetailEmployeeSerializer(many=True, read_only=True) 
    class Meta:
        model = Department
        fields = '__all__'


