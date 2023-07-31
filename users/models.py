from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.utils import timezone
from django.contrib.auth.hashers import make_password

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, full_name, phone, password=None, **extra_fields):
        if not email:
            raise ValueError("User must provide email address")
        user = self.model(email=email, full_name=full_name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,full_name,email,password,phone):
        user=self.create_user(full_name=full_name, email=self.normalize_email(email), password=password, phone=phone,)
        user.is_admin=True
        user.is_active=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):
    full_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=60)
    phone=models.CharField(max_length=15)

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['full_name','phone']

    objects = MyUserManager()

    def __str__(self):
        return self.full_name
    