from django.urls import path,include
from .views import list_orders,list_statues,update_statues,register_statues
from .views import Login_user,Logout_user,userRegister,Register_order
from rest_framework.authtoken.views import obtain_auth_token




urlpatterns = [

    path('registerUser/',userRegister,name='registerUser'),
    path('login/',Login_user, name='login'),
    path('logout/', Logout_user, name='logout'),
    path('registerOrder/',Register_order,name='RegisterS'),
    path('registerStatue/',register_statues,name='RegisterS'),
    path('listorder/',list_orders, name='ListOrder'),
    path('liststatues/', list_statues, name='ListStatues'),
    path('updatestatues/page<int:id>/',update_statues, name='UpdateStatues'),
   
]
