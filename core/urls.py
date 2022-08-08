from django.urls import path
from . import views

urlpatterns = [
    path('get-code/', views.GetVerificationCode.as_view(), name='get_verification_code'),
    path('verify/', views.VerifyCode.as_view(), name='verify_verification_code'),
]
