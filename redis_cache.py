import redis
import json

def cache_weather_data(redis_connection, cache_key, weather_data):
    redis_connection.set(cache_key, json.dumps(weather_data))

def retrieve_weather_data(redis_connection, cache_key):
    data = redis_connection.get(cache_key)
    if data:
        return json.loads(data)
    return None
