from database.redisdb import redis
from pydantic import BaseModel, Field
from typing import List,Optional
from fastapi import File,UploadFile

class CheckToxicComment(BaseModel):    
    txt: str = Field(...)
    
class CheckToxicCommentInFile(BaseModel):
    txt: UploadFile = File(...)


