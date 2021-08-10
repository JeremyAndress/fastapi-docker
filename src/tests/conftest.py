import pytest
from fastapi.testclient import TestClient

from main import app
from core.role import ROLE
from models import Base, Rol
from core.config import settings
from core.security import create_access_token
from db.session import get_db, SessionLocal, engine
from api.api_v1.auth.controller import authenticate

@pytest.fixture(scope="session")
def test_db():
    try:
        Base.metadata.create_all(bind=engine)
        yield SessionLocal()
    finally:
        for tbl in reversed(Base.metadata.sorted_tables):
            engine.execute(tbl.delete())


@pytest.fixture(scope="session")
def create_roles(test_db):
    objects = [
        Rol(id=1, name=ROLE.ADMIN.value),
        Rol(id=2, name=ROLE.BASIC.value),
    ]
    test_db.add_all(objects)
    test_db.commit()


@pytest.fixture(scope="module")
def client(test_db):
    def _test_db():
        return test_db
    app.dependency_overrides[get_db] = _test_db
    with TestClient(app) as client:
        yield client


@pytest.fixture(scope="module")
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


@pytest.fixture(scope="module")
def super_user_token(test_db, create_super_user):
    if authenticate(
        test_db, username=settings.TEST_SUPER_USER_USERNAME,
        password=settings.TEST_SUPER_USER_PASSWORD
    ):
        return create_access_token(settings.TEST_SUPER_USER_USERNAME)
