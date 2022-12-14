import pyotp
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from core import managers


class User(AbstractUser):
    mobile_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}$',
                                  message="Phone number must not consist of space and requires country code. eg : +2559125855")

    # model field start here

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
