from django import forms
from .models import Order,Statues

class orderform(forms.ModelForm):
    class Meta :
        model=Order

        field =[
            'name_customer',
            'cin',
            'adress_customer',
            'adress_recipient',
            'nature_of_package',
            'number_phone_customer',
        ]

class statusform(forms.ModelForm):
    class Meta :
        model=Statues

        field=[
            'user',
            'order',
            'statue',
        ]     