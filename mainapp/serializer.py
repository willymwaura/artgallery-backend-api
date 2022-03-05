from rest_framework import  serializers
from . models import Product,User,Notification,Cart
       
class Productserializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
class Cartserializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields='__all__'

class Notificationserializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'

