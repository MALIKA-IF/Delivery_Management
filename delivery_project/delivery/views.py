from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import orderform,statusform,loginform,registrationform
from .models import Order,Statues
from django.contrib import messages
from rest_framework.decorators import api_view,APIView
from .serializers import loginSerializer,RegisterSerializer,RegisterOrderSerializer,RegisterStatuesSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.

@api_view(['POST'])
def userRegister(requset):
    if requset.method =="POST":
        serializer =RegisterSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"sign up succefully"})  
        return Response(serializer.errors)               



@api_view(['POST'])
def Login_user(request):

    if request.method == "POST":
       serializer = loginSerializer(data=request.data)
       if serializer.is_valid():
          user=authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
    if user is not None:
        token, created=token.object.create(user=user)
        return Response({'token',token.key})
    return Response(serializer.errors)
        
   

@api_view(['POST'])
def Logout_user(request):
   if request.method=='POST':
       request.user.auth_token.delete()
       return Response({"message":"you logged out"})


@api_view(['POST'])   
def Register_order(request):
   
    serializer = RegisterOrderSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
    return Response({"message":"order register succefully"})  

 

        
@api_view(['GET'])
def list_orders(request):
    orders= Order.objects.all()
    serializer = RegisterOrderSerializer(orders,many=True)
    result={
        "data":serializer.data
    }

    return Response(result,status=status.HTTP_200_OK)


@api_view(['GET'])
def list_statues(request):
    statues = Statues.objects.all()
    serializer = RegisterStatuesSerializer(statues,many=True)
    result={
        "data":serializer.data
    }

    return Response(result,status=status.HTTP_200_OK)

@api_view(['POST'])
def register_statues(request):
    serializer = RegisterStatuesSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()
       return Response({"message":"statue register succefully"})  



def update_statues(request, id):

    pass
