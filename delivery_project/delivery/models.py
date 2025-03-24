from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    name_customer=models.CharField(max_length=20)
    cin = models.CharField(max_length=10)
    adress_customer=models.CharField(max_length=200)
    adress_recipient=models.CharField(max_length=200)
    nature_of_package=models.CharField(max_length=100)
    number_phone_customer=models.IntegerField()

class Statues(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    STATUS_Processing = ""
    STATUS_Out = ""
    STATUS_Completed= ""
    STATUS_CHOICES = [
        (STATUS_Processing, 'processing'),
        (STATUS_Out, 'out for delivery'),
        (STATUS_Completed, 'completed'),]
    statue = models.IntegerField(choices=STATUS_CHOICES)
                             
