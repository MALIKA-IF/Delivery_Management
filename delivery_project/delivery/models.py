from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    name_customer=models.CharField(max_length=20)
    cin = models.CharField(max_length=10)
    adress_customer=models.CharField(max_length=200)
    adress_recipient=models.CharField(max_length=200)
    nature_of_package=models.CharField(max_length=100)
    number_phone_customer=models.IntegerField()

    def __str__(self):
        return self.name_customer

class Statues(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    
 
    STATUS_CHOICES = [
        (1, 'processing'),
        (2, 'out for delivery'),
        (3, 'completed'),]
    statue = models.IntegerField(choices=STATUS_CHOICES)
                             