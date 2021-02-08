import hashlib
import json

from typing import Dict, Any

def generate_hash(json_dict: Dict[str, Any]) -> str:
    json_dict = json.dumps(json_dict, sort_keys=True).encode("utf-8")
    return hashlib.md5(json_dict).hexdigest()