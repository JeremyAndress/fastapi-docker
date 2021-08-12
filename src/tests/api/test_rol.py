
def test_create_role(client, super_user_token):
    data = {
        'name': 'new_role'
    }
    response = client.post(
        '/api/v1/role', json=data, headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 201, response.text
    response_json = response.json()
    expected_data = {'name': 'new_role', 'id': 3}
    assert response_json == expected_data


def test_get_role(client, super_user_token):
    response = client.get(
        '/api/v1/role/1', headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    expected_data = {'name': 'ADMINISTRATOR', 'id': 1}
    assert response_json == expected_data


def test_get_roles(client, super_user_token):
    response = client.get(
        '/api/v1/roles?page=1', headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    expected_data = {
        'previous_page': None, 'next_page': None, 'total': 2,
        'pages': 1, 'data': [
            {'name': 'ADMINISTRATOR', 'id': 1},
            {'name': 'BASIC', 'id': 2}
        ]
    }
    assert response_json == expected_data


def test_update_role(client, super_user_token):
    data = {'name': 'new_name', 'id': 2}
    response = client.put(
        '/api/v1/role', json=data,
        headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    assert response_json == data


def test_delete_role(client, super_user_token):
    response = client.delete(
        '/api/v1/role/2',
        headers={
            'token': super_user_token
        }
    )
    assert response.status_code == 200, response.text
    response_json = response.json()
    expected_data = {'name': 'BASIC', 'id': 2}
    assert response_json == expected_data
