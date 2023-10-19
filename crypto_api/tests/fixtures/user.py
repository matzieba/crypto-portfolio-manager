from model_bakery import baker
import pytest
from rest_framework.test import APIClient

from crypto_api.models import User


@pytest.fixture()
def user():
    return baker.make(User)


@pytest.fixture()
def user_create_data():
    return {
        "first_name": "John",
        "last_name": "Smith",
        "password": "password",
        "email": "user@example.com",
    }


@pytest.fixture()
def rest_client():
    return APIClient()


@pytest.fixture()
def auth_client(rest_client):
    def auth_user(user):
        rest_client.force_authenticate(user)
        return rest_client

    return auth_user
