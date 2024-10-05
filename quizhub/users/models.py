from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class RegisterUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    
    
   
    
    class Meta: 
        app_label = 'users'
    
   
    
    
