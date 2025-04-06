from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import orderform,statusform,loginform,registrationform
from .models import Order,Statues
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import loginSerializer,RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework import response

# Create your views here.
@api_view(['POST'])
def userRegister(requset):
    if requset.method =="POST":
        serializer =RegisterSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return response({"message":"sign up succefully"})  
        return response(serializer.errors)               

    pass


@api_view(['POST'])
def Login_user(request):
    if request.method == "POST":
       serializer = loginSerializer(data=request.data)
       if serializer.is_valid():
          user=authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
    if user is not None:
        token, created=token.object.create(user=user)
        return response({'token',token.key})
    return response(serializer.errors)
        
    
    
    
@api_view(['POST'])
def Logout_user(request):
   if request.method=='POST':
       request.user.auth_token.delete()
       return response({"message":"you logged out"})
   


#function to register orders by customers
def register_order(request):

    context={}

    form = orderform(request.POST)
    if form.is_valid():
        form.save()

    context['form']= form   
    return render(request,'delivery/RegisterOrder.html',context)

def register_statues(request):

    context={}

    form = statusform(request.POST)
    if form.is_valid():
        form.save()

    context['form']= form   
    return render(request,'delivery/RegisterStatues.html',context)

#function to update statues by drivers
def update_statues(request, id):

    context={}
    stat=get_object_or_404(Statues,id=id)

    form =statusform(request.POST, instance=stat)
    if form.is_valid():
        form.save()
    context["form"]=form

    return render(request,'delivery/update_statues.html', context)
        
#function to retrieve all customers orders
def list_orders(request):

    context={}

    context['dataset']=Order.objects.all()

    return render(request,'delivery/list_orders.html',context)

#function to retrieve all customers orders by driver id
#def list_orders(request,id):

 #   context={}

#    context['dataset']=Order.objects.all()

#    return render(request,'delivery/list_orders.html',context)

#function to retrieve all orders statues
def list_statues(request):

    context={}

    context['dataset']=Statues.objects.all()

    return render(request,'delivery/list_statues.html',context)

