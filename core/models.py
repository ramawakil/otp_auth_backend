from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=14, help_text='Phone Number', unique=True)
    verification_code = models.CharField(max_length=6, help_text='Verification Code')
    user_key = models.CharField(max_length=500, unique=True, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'
