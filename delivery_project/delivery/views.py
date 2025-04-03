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


#function to register orders by customers
def register_order(request):

    context={}

    form = orderform(request.POST)
    if form.is_valid():
        form.save()

    context['form']= form   
    return render(request,'delivery/RegisterOrder.html',context)

#function to update statues by drivers
def update_statues(request):

    from1 =statusform(request.POST)
    
    pass    
#function ti retrieve all customers orders
def list_orders(request):

    context={}

    context['dataset']=Order.objects.all()

    return render(request,'delivery/list_orders.html',context)

#function to retrieve all orders statues
def list_statues(request):

    context={}

    context['dataset']=Statues.objects.all()

    return render(request,'delivery/list_statues.html',context)

