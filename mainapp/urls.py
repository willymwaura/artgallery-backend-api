from django.urls import URLPattern, path
from . import views
from . views import allusers,allproducts, deletenotification,deleteuser,deleteproduct,addnotification,addtocart,deletefromcart, getproductid, getuserbyid

urlpatterns = [
    path('allusers/',allusers.as_view()),
    path('allproducts/',allproducts.as_view()),
    path('deleteuser/<int:pk>',deleteuser.as_view()),
    path('deleteproduct/<int:pk>',deleteproduct.as_view()),
    path('addtocart/',addtocart.as_view()),
    path('deletefromcart/<int:pk>',deletefromcart.as_view()),
    path('addnotification/',addnotification.as_view()),
    path('deletenotification/<int:pk>',deletenotification.as_view()),
    path('getproductid/<int:pk>',getproductid.as_view()),
    path('getuserbyid/<int:pk>',getuserbyid.as_view()),


]
