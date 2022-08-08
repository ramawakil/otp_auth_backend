from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from core.models import User
from core.serializers import PhoneNumberSerializer, VerificationCodeSerializer, UserSerializer
from helpers import send_sms, generate_time_otp


class GetVerificationCode(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = PhoneNumberSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        phone_number = request.data['phone']
        user, created = User.objects.get_or_create(phone=phone_number)
        time_otp = generate_time_otp(user)
        user.verification_code = time_otp
        user.save()

        if created:
            message = send_sms(phone_number, f"Your verification code is {time_otp}")
            return Response(dict(detail=f'SMS {message.status}'), status=201)

        else:
            message = send_sms(phone_number, f"Your verification code is {time_otp}")
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
