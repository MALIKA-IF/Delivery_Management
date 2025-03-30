from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate

# Create your views here.


def Login_user(request):
    email = request.POST['email']
    password =request.POST['password']
    user=authenticate(request, email=email, password=password)
    if user is not None:
        login(request,user)
        #redirect to the session
    

def Logout_user(request):
    logout(request)
    #redirect to login page
    
