from django.urls import URLPattern, path
from . import views
from . views import allusers,allproducts,deleteuser,deleteproduct

urlpatterns = [
    path('allusers/',allusers.as_view()),
    path('allproducts/',allproducts.as_view()),
    path('deleteuser/<int:pk>',deleteuser.as_view()),
    path('deleteproduct/<int:pk>',deleteproduct.as_view())

]
