from pydantic import BaseModel
from typing import Optional, Dict

class ActivityLog(BaseModel): 
    operationName: Optional[str] = ''
    query: str = ''
    variables: Optional[Dict] = {}