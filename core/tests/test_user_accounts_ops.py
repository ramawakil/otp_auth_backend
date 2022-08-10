import pytest
from core.models import User
from rest_framework import status
from model_bakery import baker


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
