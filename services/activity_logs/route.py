from fastapi import APIRouter, Body, Request
from .model import ActivityLog
from connect.redis_connection import redis
import config
import time
import jwt
import hashlib

cfg = config.Settings()

router = APIRouter()

@router.post("/")
async def activity_log(request: Request, payload: ActivityLog = Body(...)):     
    start = time.time()
    headers = {"{}".format(key):request.headers.get(key) for key in request.headers.keys()}       
    variables = {}
    decoded = {}
    session = ""

    if "Authorization" in headers:
        session = headers["Authorization"]
        session = hashlib.sha256(b"session").hexdigest()
        token = headers["Authorization"].replace("Bearer","")
        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
        except Exception as error:
            print(error)   

    if (payload.variables and "password" in payload.variables):
        del payload.variables["password"]
        variables = payload.variables    

    data_log = {
        "time": start,
        "query": payload.query if payload.query else "",
        "values": variables,
        "url": "{}".format(request.url),
        "method": request.method,
        "session": session,
        "header": headers,
        "userInfor": decoded
    }   

    redis.publish(cfg.redis_channel, data_log)

    return data_log 

