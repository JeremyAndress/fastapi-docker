from test import (
    client, Rol,
    TestingSessionLocal, engine, Base
)


def test_create_rol():
    db = TestingSessionLocal()
    rol_test = Rol(name='admin')
    db.add(rol_test)
    db.commit()
    db.refresh(rol_test)
    db.close()
    print(rol_test)
    assert rol_test.id, 'Error al crear rol'
 

def test_create_user():
    response = client.post(
        '/api/v1/user',
        json={
            "username": "jeremy",
            "password": "jeremy",
            "rol_id": 1
        }
    )
    print(response.text)
    assert response.status_code == 200, response.text


def test_login_user():
    response = client.post(
        '/api/v1/login/',
        json={
            "username": "jeremy",
            "password": "jeremy"
        }
    )
    assert response.status_code == 200, response.text
    res_json = response.json()
    assert res_json['access_token']
    return res_json


def test_get_all_user():
    credentials = test_login_user()
    print(f'credentials {credentials}')

    response = client.get(
        '/api/v1/users?page=1',
        headers={
            "token": credentials['access_token']
        }
    )
    print(f'response {response.text}')
    assert response.status_code == 200, response.text



def test_clean_database():
    for tbl in reversed(Base.metadata.sorted_tables):
        print(tbl)
        engine.execute(tbl.delete())