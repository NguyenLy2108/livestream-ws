from database.redisdb import redis
from typing import List, Optional
from fastapi import APIRouter, Body , Query, Depends, Path
from fastapi.encoders import jsonable_encoder
import json
import asyncio


from .model import InsertToxicComment, GetToxicComment, UpdateToxicComment


router = APIRouter()

async def check_key(key_name:str):   
    return await redis.exists(key_name)

@router.post("/")
async def add_toxic_cmt(payload: InsertToxicComment = Body(...)):  
    cmt_key = await payload.make_key()
    cmt_value = payload.value
    
    return await redis.set(cmt_key, cmt_value)

@router.get("/")
async def get_toxic_cmt(payload: GetToxicComment = Depends()):
    condition = await payload.get_param()
    data = await redis.mget(condition)    
    
    return data

@router.put("/")
async def update_toxic_cmt(key: str, payload: UpdateToxicComment = Body(...)):
    if await check_key(key) == 1:
        await redis.set(key, payload.value)
        return await redis.get(key)
    return 'Not OK'

@router.delete("/")
async def delete_toxic_cmt(key:str):
    if await check_key(key) == 1:
        await redis.delete(key)
        return 'Del OK'
    
    return "Not OK"
   