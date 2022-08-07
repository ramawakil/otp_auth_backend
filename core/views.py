from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from twilio.rest import TwilioClient

account_sid = 'AC575a5213bdead761fbf816855f02dbb6'
auth_token = 'fbe1d0710c8dc7513107da5e7dcba255'
twilio_phone = '+19706844891'
client = TwilioClient(account_sid, auth_token)


class GetVerificationCode(generics.CreateApiView):

