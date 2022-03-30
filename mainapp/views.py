


from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse, request, response
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.views import Response
from mainapp.models import Cart, Notification, User,Product,Mpesa
from mainapp.serializer import Cartserializerid, Userserializer,Productserializer,Cartserializer,Notificationserializer,Mpesaserializer,Useserializer
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from  mainapp.mpesa_credentials import LipanaMpesaPpassword , MpesaAccessToken 
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate


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

class gettoken(APIView):
    def post(self,request):
        consumer_key = 'cHnkwYIgBbrxlgBoneczmIJFXVm0oHky'
        consumer_secret = '2nHEyWSD4VjpNh2g'
        api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
        mpesa_access_token = json.loads(r.text)
        validated_mpesa_access_token = mpesa_access_token['access_token']
        return HttpResponse(validated_mpesa_access_token)
class lipanampesa(APIView):
    def post(self,request):
        serializer=Mpesaserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
        Amount=Mpesa.objects.last().Amount
        print(Amount)
        phone=Mpesa.objects.last().PhoneNumber
        print(phone)
        access_token = MpesaAccessToken.validated_mpesa_access_token
        

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount":Amount,
            "PartyA":phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber":phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Art Gallery Software company",
            "TransactionDesc": "Testing stk push"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)

class LoginView(APIView):
    def post(self,request):
        if 'email' in request.data:
            ema=request.data['email']
        else :
            ema=False
        if 'password' in request.data:
            pas=request.data['password']
        else :
            pas=False
        email = User.objects.values_list('email',flat=True)
        password = User.objects.values_list('password',flat=True)
        
        if ema in email and pas in password:
            a=User.objects.get(email=ema)
            serializer=Useserializer(a)
            return Response (serializer.data)


        else:
            return HttpResponse("fail")
        
class getcartid(APIView):
   def get(self,request,pk):
      s=Cart.objects.filter(user_id=pk)
      serializers=Cartserializerid(s,many=True)
      return Response(serializers.data)