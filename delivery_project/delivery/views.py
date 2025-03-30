from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from .forms import orderform,statusform
from .models import Order,Statues

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
    return render(request,"login.html")

def register_order(request):

    context={}

    form = orderform(request.POST)
    if form.is_valid():
        form.save()

    context['form']= form   
    return render(request,'RegisterOrder.html',context)


def register_statues():
    pass    
