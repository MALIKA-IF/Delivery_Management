from django import forms
from .models import Order,Statues
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.models import User


class registrationform(UserCreationForm):
    
    class Meta :
        model = User
        fields =[
            'username',
            'password1',
            'password2'
        ]
    

class loginform(AuthenticationForm):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    
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

       

      