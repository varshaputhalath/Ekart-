from django import forms
from django.contrib.auth.models import User
from UserApp.models import Cart,Orders

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
        }

class SigninForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}),
        }

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['quantity']
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control','placeholder':'Quantity'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=['address','email']
        widgets={
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email','type':'email'}),

        }