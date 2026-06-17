from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_database
from app.schemas.user import UserResponse
from app.services.user_service import get_all_users, get_user_by_id, update_user_profile


router = APIRouter(prefix="/users", tags=["Users"])


TEMP_USER_ID = 1


@router.get("/me", response_model=UserResponse)
def get_my_profile(db: Session = Depends(get_database)):
    user = get_user_by_id(db, TEMP_USER_ID)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.put("/me", response_model=UserResponse)
def update_my_profile(full_name: str, db: Session = Depends(get_database)):
    user = update_user_profile(db, TEMP_USER_ID, full_name)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_database)):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )

    return user


@router.get("/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_database)):
    return get_all_users(db, skip=skip, limit=limit)
