from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#class NameForm(forms.Form):
 #   name=forms.CharField(label="your name", max_length=50)
 #   def save(self):
 #       pass

# class User(models.Model):
#     username=models.CharField(max_length=100)
#     password=models.CharField(max_length=100)
#     email=models.EmailField(null=True)

#     def __str__(self):
#         return self.username

# class UserDetails(models.Model):
#     username=models.CharField(max_length=100)
#     firstname=models.CharField(max_length=100)
#     email=models.EmailField(max_length=100)
#     lastname=models.CharField(max_length=100)
#     address=models.CharField(max_length=300)

class SignUp(models.Model):
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    lastname=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    password=models.CharField(max_length=100)



