from fastapi import Request, HTTPException
import time

rate_store = {}

async def rate_limiter(request: Request, limit=20, window=60):
    ip = request.client.host
    current_time = time.time()

    if ip not in rate_store:
        rate_store[ip] = []

    # Remove expired entries
    rate_store[ip] = [t for t in rate_store[ip] if t > current_time - window]

    if len(rate_store[ip]) >= limit:
        raise HTTPException(status_code=429, detail="Too many requests, slow down.")

    rate_store[ip].append(current_time)
  
