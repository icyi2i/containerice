from redis import Redis
from flapp.common.config import REDIS_CONFIG


def connect_redis_instance():
    try:
        redis_connection = Redis(**REDIS_CONFIG)
        redis_connection.time()
        return redis_connection
    except Exception as e:
        print("Could not establish database connection.", e)
        return None
