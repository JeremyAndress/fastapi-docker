import pytest
from fastapi.testclient import TestClient

from main import app
from core.role import ROLE
from models import Base, Rol
from core.config import settings
from core.security import create_access_token
from db.session import get_db, SessionLocal, engine
from api.api_v1.auth.controller import authenticate
from tests.utils.user import create_super_user, create_basic_user # noqa F401


@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    yield SessionLocal()
    for table in reversed(Base.metadata.sorted_tables):
        engine.execute(table.delete())


@pytest.fixture
def create_roles(test_db):
    objects = [
        Rol(id=1, name=ROLE.ADMIN.value),
        Rol(id=2, name=ROLE.BASIC.value),
    ]
    test_db.add_all(objects)
    test_db.commit()


@pytest.fixture
def client(test_db):
    def _test_db():
        return test_db
    app.dependency_overrides[get_db] = _test_db
    return TestClient(app)


@pytest.fixture
def super_user_token(
    test_db,
    create_super_user # noqa F811
):
    if authenticate(
        test_db, username=settings.TEST_SUPER_USER_USERNAME,
        password=settings.TEST_SUPER_USER_PASSWORD
    ):
        return create_access_token(settings.TEST_SUPER_USER_USERNAME)


@pytest.fixture
def basic_user_token(
    test_db,
    create_basic_user # noqa F811
):
    if authenticate(
        test_db, username=settings.TEST_USER_USERNAME,
        password=settings.TEST_USER_PASSWORD
    ):
        return create_access_token(settings.TEST_USER_USERNAME)
