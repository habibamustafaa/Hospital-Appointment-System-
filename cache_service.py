import redis
from app.config import REDIS_HOST, REDIS_PORT

# redis connection
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

def set_cache(key, value):
    # cache expires after 60 seconds
    r.set(key, value, ex=60)

def get_cache(key):
    return r.get(key)

def delete_cache(key):
    # used for invalidation after updates
    r.delete(key)