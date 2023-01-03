import json
import os

REDIS_HOST = os.environ.get("REDIS_HOST") or "localhost"
REDIS_PORT = os.environ.get("REDIS_PORT") or 6379
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or ""
REDIS_DATABASE = os.environ.get("REDIS_DATABASE") or 0

REDIS_CONFIG = {
    "host": REDIS_HOST,
    "port": REDIS_PORT,
    "password": REDIS_PASSWORD,
    "db": REDIS_DATABASE,
}


DATATYPE_KEY_CAST_MAP = {
    "I": int,
    "F": float,
    "S": str,
    "D": json.loads,
    "L": json.loads,
}

DATATYPE_CLASS_KEY_MAP = {
    int: "I",
    float: "F",
    str: "S",
    dict: "D",
    list: "L",
}
