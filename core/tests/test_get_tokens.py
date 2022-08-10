import pytest
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


@pytest.fixture
def user_accounts(api_client):
    def do_create_user(user_detail_obj):
        return api_client.post('/api/v1/users/', user_detail_obj)
    return do_create_user


@pytest.mark.django_db
class TestCreateAccount:

    def test_if_user_is_anonymous_returns_401(self, user_accounts):
        response = user_accounts({'phone': '+254712345678'})

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_authenticated_returns_201(self, authenticate_user, user_accounts):
        authenticate_user(is_staff=True, is_active=True)
        response = user_accounts({'phone': '+254712345678'})

        assert response.status_code == status.HTTP_201_CREATED
