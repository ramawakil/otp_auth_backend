from django.urls import path
from rest_framework import routers

from . import views

user_router = routers.SimpleRouter()
user_router.register('users', views.UserViewSet)

urlpatterns = [
    path('get-code/', views.GetVerificationCode.as_view(), name='get_verification_code'),
    path('verify/', views.VerifyCode.as_view(), name='verify_verification_code'),
]

urlpatterns += user_router.urls

