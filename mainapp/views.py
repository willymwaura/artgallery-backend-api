import rest_framework
from django.shortcuts import render
from django.http import HttpResponse, request, response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.views import Response
from mainapp.models import User,Product,Artcategory,Usercategory
from mainapp.serializer import Artcategoryserializer, Userserializer,Productserializer,Usercategoryserializer

# Create your views here.
class allproducts(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response (serializer.data)

    def post(self,request):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)

class allusers(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=Userserializer(users,many=True)
        return Response (serializer.data)

    def post(self,request,pk):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data)
class deleteproduct(APIView):
    def delete(Self,request,pk):
        product=Product.objects.get(id=pk)
        product.delete()
        return Response("deleted")
class deleteuser(APIView):
    def delete(Self,request,pk):
        user=User.objects.get(id=pk)
        user.delete()
        return Response('Deleted')




