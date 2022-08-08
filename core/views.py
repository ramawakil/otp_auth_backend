import pyotp
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from twilio.rest import Client

from core.models import User
from core.serializers import PhoneNumberSerializer, VerificationCodeSerializer, UserSerializer

account_sid = 'AC575a5213bdead761fbf816855f02dbb6'
auth_token = 'fbe1d0710c8dc7513107da5e7dcba255'
twilio_phone = '+19706844891'
client = Client(account_sid, auth_token)


class GetVerificationCode(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        phone_number = request.data['phone']
        user, created = User.objects.get_or_create(phone=phone_number)
        time_otp = pyotp.TOTP(user.user_key, interval=600)
        time_otp = time_otp.now()
        print(time_otp)
        user.verification_code = time_otp
        user.save()
        if created:
            message = client.messages.create(
                body=f"Your verification code is {time_otp}",
                from_=twilio_phone,
                to=phone_number
            )
            return Response(dict(detail=f'SMS {message.status}'), status=201)

        else:
            message = client.messages.create(
                body=f"Your verification code is {time_otp}",
                from_=twilio_phone,
                to=phone_number
            )
            return Response(dict(detail=f'SMS {message.status}'), status=201)


class VerifyCode(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = VerificationCodeSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        verification_code = request.data['verification_code']
        user = User.objects.filter(verification_code=verification_code).first()
        if user.authenticate(verification_code):
            refresh = RefreshToken.for_user(user)
            return Response(dict(detail={
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }), status=400)
        else:
            return Response(dict(detail='Invalid code'), status=400)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

