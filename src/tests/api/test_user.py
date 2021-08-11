
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
    response_json = response.json()
    expected_data = {
        'username': 'test_user',
        'rol_id': 1, 'email': 'test@gmail.com', 'id': 1
    }
    assert response_json == expected_data


def test_get_users(client, super_user_token):
    response = client.get(
        '/api/v1/users?page=1', headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    expected_data = {
        'previous_page': None, 'next_page': None, 'total': 1,
        'pages': 1, 'data': [
            {
                'username': 'test_super_user', 'rol_id': 1,
                'email': 'test_super_user@gmail.com', 'id': 1
            }
        ]
    }
    assert response_json == expected_data


def test_update_user(client, super_user_token, create_basic_user):
    data = {
        'username': 'test_user',
        'password': 'test_1234',
        'email': 'test@gmail.com',
        'rol_id': 1,
        'id': 2
    }
    response = client.put(
        '/api/v1/user', json=data,
        headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    del data['password']
    assert response_json == data


def test_delete_user(client, super_user_token, create_basic_user):
    response = client.delete(
        '/api/v1/user/2',
        headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    expected_data = {
        'username': 'test_user', 'rol_id': 2,
        'email': 'test_user@gmail.com', 'id': 2
    }
    assert response_json == expected_data
