import asyncio
from dataclasses import dataclass
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@dataclass
class UserInfo:
    id: int
    name: str
    score: int


users: Dict[int, UserInfo] = {
    1: UserInfo(1, "Amir", 12),
    2: UserInfo(2, "Alex", 15),
    3: UserInfo(3, "Sara", 9),
}


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    await asyncio.sleep(0.2)  # for exaggeration
    if user_id in users:
        return {"ok": True, "user": users[user_id]}
    return {"ok": False, "error": "user not founded"}
