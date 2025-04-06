from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    
    password=serializers.CharField()
    password2=serializers.CharField()
    class Meta:
        model=User
        fields=('username','password', 'password2')

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
        password=serializers.CharField()