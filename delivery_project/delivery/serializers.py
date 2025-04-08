from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Order,Statues


class RegisterSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField()
    password2=serializers.CharField()
    class Meta:
        model=User
        fields= ['username','password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Error!')
        return data
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    
class loginSerializer(serializers.ModelSerializer):
        username=serializers.CharField()
        password=serializers.CharField(write_only=True)

        
class RegisterOrderSerializer(serializers.ModelSerializer):
     class Meta:
        model=Order
        fields= ['name_customer','cin', 'adress_customer','adress_recipient',
                 'nature_of_package','number_phone_customer'       
                 ]    
     def create(self, validated_data):
          order=Order.objects.create(**validated_data)
          return order
     
class RegisterStatuesSerializer(serializers.ModelSerializer):
     class Meta:
          model=Statues
          field= ['user','order','statue']
     def create(self, validated_data):
          statue=Statues.objects.create(**validated_data)
          return statue

    
 
    