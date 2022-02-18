from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import EmailValidator

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        """Creates and saves a new user """
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_superuser(self, email, password, **kwargs):
        """Creates a new super user """
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that suppports using email instead username"""
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator(message="email format is not valid")])
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


