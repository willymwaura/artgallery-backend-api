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
    designer_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    user_id=models.IntegerField(null=True)
    product_id=models.IntegerField(default=1)

    def __str__(self):
        return '{}{}'.format(self.name,self.category)

class Notification(models.Model):
    message=models.CharField(max_length=200)
    title=models.CharField(max_length=200)
    user_id=models.IntegerField(null=True)

    def __str__(self):
        return '{}{}'.format(self.title,self.title)
class Mpesa(models.Model):
    Amount=models.IntegerField(null=True)
    PhoneNumber=models.IntegerField()
    buyerid=models.IntegerField(null=True)
    email=models.EmailField(default='sss@gmail.com')
    pickupPoint=models.CharField(max_length=200,default='thika')


    


