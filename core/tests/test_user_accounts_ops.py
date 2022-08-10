import pytest
from model_bakery import baker
from rest_framework import status

from core.models import User


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


@pytest.mark.django_db
class TestRetrieveAccount:
    """
    I'm not sure if this is the best way to test this
    but to reuse the above test pattern (same url to create user) could lead to several errors if above test are
    not implemented correctly for this I'm sticking with this way of testing only one thing in a single test implementation
    """

    def test_if_user_exists_returns_200(self, api_client):
        user = baker.make(User)
        api_client.force_authenticate(user=user)
        response = api_client.get(f'/api/v1/users/{user.id}/')

        assert response.status_code == status.HTTP_200_OK

    def test_if_user_does_not_exist_returns_404(self, api_client, authenticate_user):
        authenticate_user(is_staff=True, is_active=True)
        response = api_client.get('/api/v1/users/1/')
        assert response.status_code == status.HTTP_404_NOT_FOUND



@pytest.mark.django_db
class TestGetCode:

    def test_request_token_to_login_or_register(self, api_client, authenticate_user):
        authenticate_user(is_staff=True, is_active=True)
        response = api_client.post('/api/v1/get-code/', {'phone': '+254712345678'})

        assert response.status_code == status.HTTP_201_CREATED

