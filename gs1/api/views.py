from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

def student_details(request, pk):
    stu = Student.objects.get(id = pk)
    serialier = StudentSerializers(stu)
    # json_data = JSONRenderer().render(serialier.data)
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serialier.data)

def student_details_all(request):
    stu = Student.objects.all()
    serialier = StudentSerializers(stu, many = True)
    # json_data = JSONRenderer().render(serialier.data)
    # return HttpResponse(json_data,content_type = 'application/json')
    return JsonResponse(serialier.data, safe=False)
    