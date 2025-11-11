import jwt
SECRET = "omnicore_secret"
def create_token(data): return jwt.encode(data, SECRET, algorithm="HS256")
