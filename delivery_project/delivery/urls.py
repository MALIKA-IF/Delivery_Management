from django.urls import path
from .views import Login_user,Logout_user,register_order,list_orders,list_statues

urlpatterns = [

    path('login/', Login_user, name='login'),
    path('logout/', Logout_user, name='logout'),
    path('register/',register_order,name='Register'),
    path('listorder/',list_orders, name='ListOrder'),
    path('liststatues/', list_statues, name='ListStatues')
    

    
]
