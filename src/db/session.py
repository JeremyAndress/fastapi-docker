from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from utils.logging import logger

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True, 
    connect_args={'connect_timeout': 3}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    except Exception as e:
        logger.error(f'error - {e}')
    finally:
        db.close()
