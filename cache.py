import redis
import json

cache = redis.StrictRedis(host='localhost', port=6379, db=0)

def get_from_cache(domain_name):
    data = cache.get(domain_name)
    if data:
        return json.loads(data)
    return None

def set_in_cache(domain_name, data):
    cache.set(domain_name, json.dumps(data), ex=3600)  # Кэш на 1 час
