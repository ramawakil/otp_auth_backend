import pyotp
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import User


def is_unique(key):
    """
    check the user model if key is unique
    """
    try:
        User.objects.get(user_key=key)
    except User.DoesNotExist:
        return True
    return False


def generate_unique_user_key_for_otp():
    """
    if key is not unique, generate new key recursively
    """
    key = pyotp.random_base32()
    if is_unique(key):
        return key
    generate_unique_user_key_for_otp()


@receiver(post_save, sender=User)
def create_user_key(sender, instance, **kwargs):
    """
    create keys for new user
    """
    if not instance.user_key:
        instance.user_key = generate_unique_user_key_for_otp()
        instance.save()
