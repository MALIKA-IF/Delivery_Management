from django.urls import path
from .views import Login_user,Logout_user

urlpatterns = [
    path('login/', Login_user, name='login'),
    path('logout/', Logout_user, name='logout'),

    
]
