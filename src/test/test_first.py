from test import client,Rol,TestingSessionLocal

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
        '/api/v1/user/user_create/',
        json={
            "username":"jeremy",
            "password":"password",
            "rol_id":1
        }
    )
    print(response.text)
    assert response.status_code == 200, response.text