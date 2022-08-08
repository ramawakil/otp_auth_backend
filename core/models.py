import pyotp
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from core import managers


class User(AbstractUser):
    username = models.CharField(max_length=12, blank=True, null=True)
    phone = models.CharField(max_length=14, help_text='Phone Number', unique=True)
    verification_code = models.CharField(max_length=10, help_text='Verification Code')
    user_key = models.CharField(max_length=500, blank=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'phone'

    objects = managers.UserManager()

    def authenticate(self, otp):
        try:
            time_otp = int(otp)
        except:
            return False

        t = pyotp.TOTP(self.user_key, interval=600)
        return t.verify(time_otp)
