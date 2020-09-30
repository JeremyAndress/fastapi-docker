from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from utils.logging import logger

from sqlalchemy.exc import SQLAlchemyError

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True,
     connect_args={'connect_timeout': 3}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)

def get_db():
    try:
        conn = engine.connect()
        db = SessionLocal(bind=conn)
        yield db
    except Exception as e:
        logger.error(f'Error db {e}')
    finally:
        db.close()
        conn.dispose()