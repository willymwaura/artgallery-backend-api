from django.contrib import admin

# Register your models here.

from django.contrib import admin
from.models import Artcategory,User,Usercategory,Product

# Register your models here.
admin.site.register(Artcategory)
admin.site.register(User)
admin.site.register(Usercategory)
admin.site.register(Product)


