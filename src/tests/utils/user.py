import pytest

from core.config import settings


@pytest.fixture
def create_super_user(client, create_roles):
    data = {
        'username': settings.TEST_SUPER_USER_USERNAME,
        'password': settings.TEST_SUPER_USER_PASSWORD,
        'email': f'{settings.TEST_SUPER_USER_USERNAME}@gmail.com',
        'rol_id': 1
    }
    response = client.post(
        '/api/v1/user', json=data
    )
    return response.json()


@pytest.fixture
def create_basic_user(client, create_roles):
    data = {
        'username': settings.TEST_USER_USERNAME,
        'password': settings.TEST_USER_PASSWORD,
        'email': f'{settings.TEST_USER_USERNAME}@gmail.com',
        'rol_id': 2
    }
    response = client.post(
        '/api/v1/user', json=data
    )
    return response.json()
