from django.http import HttpResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from .serializers import CreateEmployeeSerializer, MinimalEmployeeSerializer, DetailEmployeeSerializer, UpdateEmployeeSerializer
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse, JsonResponse 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EmployeeListSet(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        serializer = MinimalEmployeeSerializer(queryset, many =True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateEmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeRetrieveSet(APIView):
    def get_object(self, pk):
        return Employee.objects.get(pk=pk)
    
    def get(self, request, pk=None):
        queryset =  self.get_object(pk)    
        serializer =  DetailEmployeeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)         

    def put(self, request, pk=None):
        queryset =  self.get_object(pk) 
        serializer = UpdateEmployeeSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk=None):
        employee =  self.get_object(pk) 
        employee.delete()
        return Response(f"Employee is deleted having id {pk}", status=status.HTTP_204_NO_CONTENT)

class PositionViewSet(APIView):
    pass

class DepartmentViewSet(APIView):
    pass    