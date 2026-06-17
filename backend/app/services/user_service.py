from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_all_users(db: Session, skip: int = 0, limit: int = 20):
    return db.query(User).offset(skip).limit(limit).all()


def update_user_profile(db: Session, user_id: int, full_name: str):
    user = get_user_by_id(db, user_id)

    if not user:
        return None

    user.full_name = full_name

    db.commit()
    db.refresh(user)

    return user
