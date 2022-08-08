from abc import ABC

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from .models import User


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone']


class PhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class VerificationCodeSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['verification_code']
