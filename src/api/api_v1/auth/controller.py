from typing import Optional
from sqlalchemy.orm import Session
from api.api_v1.user.controller import get_by_email, get_by_username
from core.security import verify_password


def authenticate(
    db: Session, *, username: Optional[str] = None,
    password: str, email: Optional[str] = None
):
    user = get_by_username(
        db, username=username
    ) if username else get_by_email(db, email)

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
