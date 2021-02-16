import pytest
from faker import Faker
from test import (
    client, Rol,
    TestingSessionLocal, engine, Base
)

fake = Faker()


@pytest.mark.run(order=0)
@pytest.mark.dependency
def test_create_rol():
    db = TestingSessionLocal()
    rol_test = Rol(name='admin')
    db.add(rol_test)
    db.commit()
    db.refresh(rol_test)
    db.close()
    print(rol_test)
    assert rol_test.id, 'Error al crear rol'


@pytest.mark.run(order=1)
@pytest.mark.dependency(depends=['test_create_rol'])
def test_create_user():
    response = client.post(
        '/api/v1/user',
        json={
            "username": "jeremy",
            "password": "jeremy",
            "email": "jeremy@gmail.com",
            "rol_id": 1
        }
    )
    print(response.text)
    assert response.status_code == 201, response.text


@pytest.mark.run(order=2)
@pytest.mark.dependency(depends=['test_create_rol'])
def test_create_multiple_user():
    for i in range(10):
        response = client.post(
            '/api/v1/user',
            json={
                "username": fake.name(),
                "password": fake.name(),
                "email": fake.email(),
                "rol_id": 1
            }
        )
        print(response.text)
        assert response.status_code == 201, response.text


@pytest.mark.dependency(depends=['test_create_user'])
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


def test_delete_user():
    credentials = test_login_user()
    print(f'credentials {credentials}')

    response = client.delete(
        f'/api/v1/user/{3}',
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
