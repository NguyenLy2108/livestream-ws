from database.redisdb import redis
from typing import List, Optional
from fastapi import APIRouter, Body , Query, Depends, Path
from fastapi.encoders import jsonable_encoder
import json
import asyncio


from .model import CheckToxicComment, CheckToxicCommentInFile


router = APIRouter()


@router.post("/")
async def check_toxic_comment(payload: CheckToxicComment = Body(...)):  
    txt = payload.txt
    list_key = await redis.keys("*key_*")
    list_pat = await redis.mget(list_key)
    
    list_pat1 = list(map(lambda x: x.decode('ascii'),list_pat))
    
    
    result = "Not found toxic comments in the paragraph"
    for r in list_pat1:
        if r in txt:
            result = r
            break
    
    return result 

