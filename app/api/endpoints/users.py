import asyncio
from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status

from app.api.models.user import User

users_router = APIRouter()


@users_router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def get_user(user_id: int) -> Dict[str, str]:
    await asyncio.sleep(0.2) # simulate a slow response
    if user_id in
