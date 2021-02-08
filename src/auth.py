import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from src.secrets import BASIC_USERNAME, BASIC_PASSWORD

security = HTTPBasic()

def basic_auth(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    correct_username = secrets.compare_digest(credentials.username, BASIC_USERNAME)
    correct_password = secrets.compare_digest(credentials.password, BASIC_PASSWORD)
    if not correct_username and correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Unauthorized',
            headers={"WWW-Authenticate": "Basic"}
        )
    return credentials.username