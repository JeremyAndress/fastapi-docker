from db.session import SessionLocal
from utils.logging import logger


def init() -> None:
    try:
        db = SessionLocal()
        # Try to create session to check if DB is awake
        db.execute('SELECT 1')
    except Exception as e:
        logger.error(e)
        raise e


def main() -> None:
    logger.info('Initializing service')
    init()
    logger.info('Service finished initializing')


if __name__ == '__main__':
    main()
