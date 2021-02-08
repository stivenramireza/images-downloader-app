from pydantic import BaseModel
from typing import List, Dict, Any

class Model(BaseModel):
    images: List[Dict[str, Any]]