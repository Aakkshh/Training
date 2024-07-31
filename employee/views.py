from django.http import HttpResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from .serializers import CreateEmployeeSerializer
from rest_framework.parsers import JSONParser 

def index(request):
    return HttpResponse("Hello, world. This is the another app.")


#DJANGO dont have json but it does have dictionary

@csrf_exempt
def employee_data(request):
    if request.method == "GET":
        queryset = Employee.objects.all()#Objects
        serializer = CreateEmployeeSerializer(queryset, many=True)#Serialize 
        return HttpResponse(serializer.data, status=200)

    elif request.method == "POST":
        print("You are in POST", request.body)
        data = JSONParser().parse(request)#Parse JSON
        serializer = CreateEmployeeSerializer(data=data)#Serializer
        if serializer.is_valid():#Validate
            serializer.save()#save
            return HttpResponse("Post Method is called", serializer.data, status= 201)
# def create_employee_data(request):
    