import pytest

from core.config import settings


def test_login(client, create_super_user):
    data = {
        'username': settings.TEST_SUPER_USER_USERNAME,
        'password': settings.TEST_SUPER_USER_PASSWORD
    }
    response = client.post(
        '/api/v1/login/', json=data
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    assert response_json.get('access_token')
    del response_json['access_token']
    expected_data = {
        'token_type': 'bearer', 'rol_id': 1,
        'rol_name': 'ADMINISTRATOR'
    }
    assert response_json == expected_data


@pytest.mark.parametrize(
    "data, expected_data", [
        (
            {
                'username': settings.TEST_SUPER_USER_USERNAME,
                'password': 'fake_password'
            },
            {"detail": "Incorrect username or password"}
        ),
        (
            {
                'email': f'{settings.TEST_SUPER_USER_USERNAME}@gmail.com',
                'password': 'fake_password'
            },
            {"detail": "Incorrect email or password"}
        )
    ]
)
def test_error_login(
    client, create_super_user, data, expected_data
):
    response = client.post(
        '/api/v1/login/', json=data
    )
    assert response.status_code == 400, response.text
    response_json = response.json()
    assert expected_data == response_json
