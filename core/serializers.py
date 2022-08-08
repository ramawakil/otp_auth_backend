from rest_framework.serializers import ModelSerializer

from .models import User


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']


class PhoneNumberSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['phone']