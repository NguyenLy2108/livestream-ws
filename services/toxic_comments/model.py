from database.redisdb import redis
from pydantic import BaseModel, Field
from typing import List,Optional

class InsertToxicComment(BaseModel):    
    value: str = Field(...)
    async def make_key(self):
        key = await redis.get('cmt_key')
        counter = await redis.incr(int(key))
       
        return 'key_{}'.format(str(counter))
    
class UpdateToxicComment(BaseModel):    
    value: Optional[str]

class GetToxicComment(BaseModel):    
    key: str = Field(None)
    async def get_param(self):        
        if (self.key is None):
            condition = await redis.keys('*key_*')
        else:
            condition = self.key
       
        return condition

