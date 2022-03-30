from distutils.command.upload import upload
from django.db import models
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phonenumber=models.IntegerField()
    password=models.IntegerField()
    role=models.CharField(max_length=100)
    def __str__(self):
        return '{}{}'.format(self.name,self.role)


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.URLField(max_length=200)
    description=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    designer_id=models.IntegerField()
    designer_name=models.CharField(max_length=100)
   
    
    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Cart(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField(default=400)
    imageurl=models.URLField(max_length=200)
    category=models.CharField(max_length=100)
    designer_id=models.IntegerField(null=True)
    designer_name=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=100,null=True)

    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Notification(models.Model):
    designer=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    title=models.CharField(max_length=200)

    def __str__(self):
        return '{}{}'.format(self.designer,self.title)
class Mpesa(models.Model):
    PhoneNumber=models.IntegerField()
    Amount=models.IntegerField()


    


