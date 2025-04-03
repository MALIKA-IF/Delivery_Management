from django.shortcuts import render, get_object_or_404
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

