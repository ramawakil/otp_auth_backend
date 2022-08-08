import pyotp
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from twilio.rest import TwilioClient, Client

from core.models import User
from core.serializers import PhoneNumberSerializer

account_sid = 'AC575a5213bdead761fbf816855f02dbb6'
auth_token = 'fbe1d0710c8dc7513107da5e7dcba255'
twilio_phone = '+19706844891'
client = Client(account_sid, auth_token)


class GetVerificationCode(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        phone_number = request.data['phone_number']
        user, created = User.objects.get_or_create(phone_number=phone_number)
        print(user)
        print(created)
        if user:
            time_otp = pyotp.TOTP(user.user_key, interval=300)
            time_otp = time_otp.now()
            client.messages.create(
                body="Your verification code is " + time_otp,
                from_=twilio_phone,
                to=phone_number
            )
            return Response(dict(detail='SMS sent'), status=201)
        else:
            user = User.objects.create(phone_number=phone_number)
            user.save()
            return Response(dict(detail='SMS sent'), status=201)
