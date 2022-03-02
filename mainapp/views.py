
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request, response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.views import Response
from mainapp.models import Cart, Notification, User,Product
from mainapp.serializer import Userserializer,Productserializer,Cartserializer,Notificationserializer
from django_daraja.mpesa.core import MpesaClient

# Create your views here.
class allproducts(APIView):
    def get(self,request):
        products=Product.objects.all()
        serializer=Productserializer(products,many=True)
        return Response(serializer.data)

    def post (self,request):
        serializer=Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class allusers(APIView):
    def get(self,request):
        users=User.objects.all()
        serializer=Userserializer(users,many=True)
        return Response (serializer.data)

    def post(self,request):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
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

class addtocart(APIView):
    def get(self,request):
        products=Cart.objects.all()
        serializer=Cartserializer(products,many=True)
        return Response (serializer.data)

    def post(self,request):
        serializer=Cartserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class addnotification(APIView):
    def get(self,request):
        note=Notification.objects.all()
        serializer=Notificationserializer(note,many=True)
        return Response (serializer.data)

    def post(self,request):
        serializer=Notificationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
class deletefromcart(APIView):
    def delete(Self,request,pk):
        product=Cart.objects.get(id=pk)
        product.delete()
        return Response("deleted")
class deletenotification(APIView):
    def delete(Self,request,pk):
        product=Notification.objects.get(id=pk)
        product.delete()
        return Response("deleted")

class getproductid(APIView):
   def get(self,request,pk):
      s=Product.objects.filter(id=pk)
      serializers=Productserializer(s,many=True)
      return Response(serializers.data)

class getuserbyid(APIView):
   def get(self,request,pk):
      s=User.objects.filter(id=pk)
      serializers=Userserializer(s,many=True)
      return Response(serializers.data)


def stk(request):
    cl = MpesaClient()
    mpesa_stk_push_callback='https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query'
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = '254112100378'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = mpesa_stk_push_callback
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)

def stk_push_callback(request):
        data = request.body


