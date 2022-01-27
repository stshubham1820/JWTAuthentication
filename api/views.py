from distutils.log import error
from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.status import *
# Create your views here.
def login(request):
    return render(request,'login.html')
class Stud(APIView):#Stud is a SubClass of APIView SuperClass
    def get(self,request):
        try :
            Data = Studpersonal.objects.all()
            ser = profileserializer(Data,many=True)
            return Response(ser.data)
        except Studpersonal.DoesNotExist :
            return Response(status=status.HTTP_404_NOT_FOUND)
    def post(self,request):
        ser = profileserializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        else :
            return Response(ser.errors)
class Studpk(APIView):
    def get_object(self, pk):
        try:
            return Studpersonal.objects.get(id=pk)
        except Studpersonal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        try:
            Data = self.get_object(pk)
            ser = profileserializer(Data,many=False)
            return Response(ser.data)
        except Studpersonal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        try : 
            Data = Studpersonal.objects.get(id=pk)
            ser = profileserializer(instance=Data,data=request.data)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
            else :
                return Response(ser.errors)
        except:
            pass
    def delete(self,request,pk):
        Data = Studpersonal.objects.get(id=pk)
        Data.delete()
def home(request):
    return render(request,'index.html')
