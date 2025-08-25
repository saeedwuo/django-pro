from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser,PermissionsMixin)
from django.utils.translation import gettext_lazy as _






class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        """
        Create and save a user with the given email and password.
        """
        
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    
    def create_superuser(self,email,password,**extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        extra_fields.setdefault("is_staff", True)
        
        extra_fields.setdefault("is_superuser", True)
        
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)




class User(AbstractBaseUser,PermissionsMixin):
    """
    custom User Model for our app
    """
    email = models.EmailField(max_length=255,unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    
    def __str__(self):
        return self.email
    