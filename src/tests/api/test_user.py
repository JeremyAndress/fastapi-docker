
def test_create_user(client, create_roles):
    data = {
        'username': 'test_user',
        'password': 'test_1234',
        'email': 'test@gmail.com',
        'rol_id': 1
    }
    response = client.post(
        '/api/v1/user', json=data
    )
    assert response.status_code == 201, response.text
    data = response.json()
    excepted_data = {
        'username': 'test_user',
        'rol_id': 1, 'email': 'test@gmail.com', 'id': 1
    }
    assert data == excepted_data


def test_update_user(super_user_token):
    print(super_user_token)
