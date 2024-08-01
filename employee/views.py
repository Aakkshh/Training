from django.http import HttpResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from .serializers import CreateEmployeeSerializer, MinimalEmployeeSerializer, DetailEmployeeSerializer
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse, JsonResponse 
def index(request):
    return HttpResponse("Hello, world. This is the another app.")


#DJANGO dont have json but it does have dictionary

@csrf_exempt
def employee_data(request, pk =None):
    
    if request.method == "GET":
        if pk:
            queryset = Employee.objects.get(pk = pk)
            print(queryset)
            serializer = DetailEmployeeSerializer(queryset)
            print(serializer.data)
            return JsonResponse(serializer.data) 
        else:
            queryset = Employee.objects.all()#Objects
            serializer = MinimalEmployeeSerializer(queryset, many=True)#Serialize 
            return HttpResponse(serializer.data)

    elif request.method == "POST":
        print("You are in POST", request.body)
        data = JSONParser().parse(request)#Parse JSON
        serializer = CreateEmployeeSerializer(data=data)#Serializer
        if serializer.is_valid():#Validate
            serializer.save()#save
            print("Saving the data")
            return HttpResponse("Post Method is called", serializer.data, status= 201)
        print(serializer.errors)
        return HttpResponse(serializer.errors)
# def create_employee_data(request):


#TASK: Create endpoints which are performing CRUD operations on DEPARTMENT, POSITION, EMPLOYEE    