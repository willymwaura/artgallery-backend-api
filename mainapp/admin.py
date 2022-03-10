from django.contrib import admin

# Register your models here.

from django.contrib import admin
from.models import  Cart, Notification,User,Product,Mpesa

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Notification)
admin.site.register(Mpesa)






