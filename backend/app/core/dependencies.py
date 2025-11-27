from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import verify_token
from app.core.exceptions import InvalidTokenException

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise NotAuthenticatedException()  
    
    token = credentials.credentials
    payload = verify_token(token)
    if payload is None:
        raise InvalidTokenException()
    return payload