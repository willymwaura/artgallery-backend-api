from distutils.command.upload import upload
from django.db import models
from django.db import models
from django .utils import timezone

# Create your models here.
class Artcategory (models.Model):
    artcategory=models.CharField(max_length=100)

    def __str__(self):
        return self.artcategory

class Usercategory(models.Model):
    usercategory=models.CharField(max_length=100)

    def __str__(self):
        return self.usercategory

    


class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.IntegerField(default=400)
    accesstoken=models.CharField(max_length=100)
    refreshtoken=models.CharField(max_length=100)
    role=models.ForeignKey(Usercategory,related_name='Novels',on_delete=models.CASCADE)
    def __str__(self):
        return '{}{}'.format(self.name,self.usertype)


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.ImageField(upload_to='images',blank=False)
    in_stock=models.BooleanField
    category=models.ForeignKey(Artcategory,related_name='Textbook',on_delete=models.CASCADE)
    designer=models.ForeignKey(User,related_name='designer',on_delete=models.CASCADE)
   
    
    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Cart(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.ImageField(upload_to='images',blank=False)
    in_stock=models.BooleanField
    category=models.ForeignKey(Artcategory,related_name='Text',on_delete=models.CASCADE)
    designer=models.ForeignKey(User,related_name='cart',on_delete=models.CASCADE)

    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Notification(models.Model):
    designer=models.ForeignKey(User,related_name='note',on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    title=models.CharField(max_length=200)

    def __str__(self):
        return '{}{}'.format(self.designer,self.title)


   
    


