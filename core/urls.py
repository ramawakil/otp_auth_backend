from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetVerificationCode.as_view(), name='get_verification_code'),
]
