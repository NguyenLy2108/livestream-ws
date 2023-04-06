import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):    
    redis_host = os.getenv('REDIS_HOST')    
    redis_port = os.getenv('REDIS_PORT')
    redis_channel = os.getenv('REDIS_CHANNEL')