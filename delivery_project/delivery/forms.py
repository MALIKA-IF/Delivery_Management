from django import forms
from .models import Order,Statues
from django.contrib.auth.forms import AuthenticationForm

class loginform(AuthenticationForm):
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)

    
class orderform(forms.ModelForm):
    class Meta :
        model=Order


        fields =[
            'name_customer',
            'cin',
            'adress_customer',
            'adress_recipient',
            'nature_of_package',
            'number_phone_customer'
        ]

class statusform(forms.ModelForm):
    class Meta :
        model=Statues

        fields=[
            'user',
            'order',
            'statue'
        ]     

      