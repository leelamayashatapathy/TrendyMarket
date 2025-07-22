from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from app.core.config import rate_limit
from app.auth.jwt import get_current_user

def rate_limiter(user: str = Depends(get_current_user)):
    now = datetime.utcnow()
    wdw = timedelta(minutes=1)
    max_requests = 5  
    t_stamp = rate_limit.get(user, [])
    t_stamp = [ts for ts in t_stamp if now - ts < wdw]
    if len(t_stamp) >= max_requests:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    t_stamp.append(now)
    rate_limit[user] = t_stamp
    return user 