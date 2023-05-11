import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):  
    postgre_host = os.getenv('POSTGRE_HOST')    
    postgre_port = os.getenv('POSTGRE_PORT')
    postgre_database = os.getenv('POSTGRE_DATABASE')
    postgre_user = os.getenv('POSTGRE_USER')    
    postgre_password = os.getenv('POSTGRE_PASSWORD') 
    stream_delay = os.getenv('STREAM_DELAY')