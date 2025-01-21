from django.db import models
from AdminApp.models import Products
from django.contrib.auth.models import User


# Create your models here.
class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    date=models.DateField(auto_now_add=True)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
    )
    status=models.CharField(max_length=100,default="in-cart",choices=options)

class Orders(models.Model):
    product=models.ForeignKey(Cart,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(max_length=200)
    email=models.EmailField()
    options=(
        ('order-placed','order-placed'),
        ('cancelled','cancelled'),
        ('dispatched','dispatched'),
        ('delivered','delivered'),
    )
    status=models.CharField(max_length=100,default="order-placed",choices=options)
    date=models.DateField(auto_now_add=True)
    exp_date=models.DateField(null=True,blank=True)