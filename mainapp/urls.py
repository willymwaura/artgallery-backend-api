from django.urls import URLPattern, path
from . import views
from mainapp.views import getcartid, allusers,allproducts, deletenotification,deleteuser,deleteproduct,addnotification,addtocart,deletefromcart, getproductid, getuserbyid,lipanampesa,gettoken,LoginView
urlpatterns = [
    path('users/',allusers.as_view()),
    path('products/',allproducts.as_view()),
    path('deleteuser/<int:pk>',deleteuser.as_view()),
    path('deleteproduct/<int:pk>',deleteproduct.as_view()),
    path('cart/',addtocart.as_view()),
    path('deletecart/<int:pk>',deletefromcart.as_view()),
    path('notification/',addnotification.as_view()),
    path('deletenotification/<int:pk>',deletenotification.as_view()),
    path('getproductid/<int:pk>',getproductid.as_view()),
    path('getuserid/<int:pk>',getuserbyid.as_view()),
    path('stk',gettoken.as_view()),
    path('stkpush',lipanampesa.as_view()),
    path('login',LoginView.as_view()),
    path('cart/<int:pk>',getcartid.as_view()),
    path('notification/<int:pk>',getcartid.as_view())

]
