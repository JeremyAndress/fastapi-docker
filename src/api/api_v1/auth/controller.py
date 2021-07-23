from typing import Optional

from sqlalchemy.orm import Session

from core.security import verify_password
from api.api_v1.user.service import user_service


def authenticate(
    db: Session, *, username: Optional[str] = None,
    password: str, email: Optional[str] = None
):
    user = user_service.get_by_field(
        db, field='username', value=username
    ) if username else user_service.get_by_field(
        db, field='email', value=email
    )

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user
