from rest_framework import fields, serializers
from . models import Product,Usercategory,User,Artcategory


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