from rest_framework import  serializers
from . models import Product,User,Notification,Cart,Mpesa
       
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class Useserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','phonenumber','role']
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'
class Cartserializerid(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=['id','category','description','designer_id','designer_name','imageurl','name','price','product_id']

class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'
class Notificationserializerid(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=['id','title','message']
class Mpesaserializer(serializers.ModelSerializer):
    class Meta:
        model=Mpesa
        fields='__all__'

