from django.urls import path
from .views import register_order,list_orders,list_statues,update_statues,register_statues
from .views import Login_user,Logout_user,userRegister

urlpatterns = [

    path('registerUser/',userRegister,name='registerUser'),
    path('login/',Login_user, name='login'),
    path('logout/', Logout_user, name='logout'),
    path('register/',register_order,name='Register'),
    path('registerStatue/',register_statues,name='RegisterS'),
    path('listorder/',list_orders, name='ListOrder'),
    path('liststatues/', list_statues, name='ListStatues'),
    path('updatestatues/page<int:id>/',update_statues, name='UpdateStatues'),
    
]
