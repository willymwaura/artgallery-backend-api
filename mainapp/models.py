from distutils.command.upload import upload
from django.db import models
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.IntegerField()
    accesstoken=models.CharField(max_length=100)
    refreshtoken=models.CharField(max_length=100)
    password=models.IntegerField(default=1234)
    role=models.CharField(max_length=10)
    def __str__(self):
        return '{}{}'.format(self.name,self.role)


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.ImageField(upload_to='images',blank=False)
    description=models.CharField(max_length=100,default="lovely art")
    category=models.CharField(max_length=100)
    designer=models.CharField(max_length=100)
   
    
    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Cart(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.ImageField(upload_to='images',blank=False)
    category=models.CharField(max_length=100)
    designer=models.CharField(max_length=100)

    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Notification(models.Model):
    designer=models.ForeignKey(User,related_name='note',on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
    title=models.CharField(max_length=200)

    def __str__(self):
        return '{}{}'.format(self.designer,self.title)


   
    


