from rest_framework import fields, serializers
from . models import Product,Usercategory,User,Artcategory,Notification,Cart


class Artcategoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Artcategory
        fields='__all__'


class Usercategoryserializer(serializers.ModelSerializer):
    class Meta:
        model=Usercategory
        fields='__all__'
       
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