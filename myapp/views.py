from django.http import HttpResponse, JsonResponse
from .models import Employee, Department, Project
from .serializers import (
    CreateEmployeeSerializer, MinimalEmployeeSerializer, DetailEmployeeSerializer, UpdateEmployeeSerializer,
    DepartmentSerializer, ProjectSerializer
)
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Max, F, Subquery, OuterRef
from django.db.models import Sum


class EmployeeListSet(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        serializer = MinimalEmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentonEmployee(APIView):
    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)
    
    def get(self,request,pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        department = employee.department
        serializer = DepartmentSerializer(department)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class EmployeeRetrieveSet(APIView):
    def get_object(self, pk):
        return get_object_or_404(Employee, pk=pk)

    def get(self, request, pk=None):
        queryset = self.get_object(pk)
        serializer = DetailEmployeeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        queryset = self.get_object(pk)
        serializer = UpdateEmployeeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(f"Employee is deleted having id {pk}", status=status.HTTP_204_NO_CONTENT)

class DepartmentViewSet(APIView):
    def get(self, request):
        queryset = Department.objects.all()
        serializer = DepartmentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentRetrieveViewset(APIView):
    def get_object(self, pk):
        return get_object_or_404(Department, pk=pk)
    
    def get(self, request, pk=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department)
        employees = Employee.objects.filter(department=department)
        emp_serializer = DetailEmployeeSerializer(employees, many=True)
        response_data = serializer.data
        response_data['employees'] = emp_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
    

    def put(self, request, pk=None):
        department = self.get_object(pk)
        serializer = DepartmentSerializer(department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        department = self.get_object(pk)
        employees = Employee.objects.filter(department=department)
        if employees.exists():
            return Response({"error": "Department has employees. Cannot delete."}, status=status.HTTP_400_BAD_REQUEST)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectViewSet(APIView):
    def get(self, request, pk=None):
        if pk is None:
            queryset = Project.objects.all()
            serializer = ProjectSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            project = self.get_object(pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def add_member(self, request, pk=None):
        project = self.get_object(pk)
        employee_id = request.data.get('employee_id')
        employee = get_object_or_404(Employee, id=employee_id)
        project.team.add(employee)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update_status(self, request, pk=None):
        project = self.get_object(pk)
        status = request.data.get('status')
        project.status = status
        project.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)

class AddMemberToProjectView(APIView):
    def put(self, request, pk=None):
        project = get_object_or_404(Project, pk=pk)
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response({"error": "employee_id is required"}, status=status.HTTP_400_BAD_REQUEST)
        print(f"Employee ID: {employee_id}")
        employee = get_object_or_404(Employee, id=employee_id)
        project.team.add(employee)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class StatusOfProject(APIView):
    def get(self, request):
        print(request.query_params["status"])
        requeststatus = request.query_params["status"]
        projects = Project.objects.filter(status=requeststatus)
        serializer = ProjectSerializer(projects, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StatusOngoingProjects(APIView):
    def get(self, request):
        projects = Project.objects.filter(status="ON-GOING")
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class StatusEndedProjects(APIView):
    def get(self, request):
        projects = Project.objects.filter(status="ENDED")
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProjectBudgetView(APIView):
    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        total_budget = project.employees.aggregate(total_budget=Sum('salary'))['total_budget']
        return Response({'project_id': pk, 'total_budget': total_budget}, status=status.HTTP_200_OK)

class HighestSalaryView(APIView):
    def get(self, request):
        highest_salary = Employee.objects.aggregate(Max('salary'))['salary__max']
        employees = Employee.objects.filter(salary=highest_salary)
        serializer = DetailEmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class SecondHighestSalaryByDepartmentView(APIView):
    def get(self, request):
        subquery = Employee.objects.filter(
            department=OuterRef('department')
        ).order_by('-salary').values('salary')[1:2]

        employees = Employee.objects.annotate(
            second_highest_salary=Subquery(subquery)
        ).filter(
            salary=F('second_highest_salary')
        )

        serializer = DetailEmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TotalSalaryByDepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.annotate(
            total_salary=Sum('employee__salary')
        )

        data = [
            {
                'department_id': department.id,
                'department_name': department.name,
                'total_salary': department.total_salary
            }
            for department in departments
        ]

        return Response(data, status=status.HTTP_200_OK)
