from json import JSONDecodeError, loads
from typing import Any

from flapp.common.config import (
    DATATYPE_KEY_CAST_MAP,
    DATATYPE_CLASS_KEY_MAP,
)


def format_redis_value(value: Any = None) -> str:
    try:
        data_key = DATATYPE_CLASS_KEY_MAP[type(loads(value))]

    except JSONDecodeError:
        data_key = DATATYPE_CLASS_KEY_MAP[str]

    return f"{data_key}::{str(value)}"


def parse_redis_value(value: bytes = None) -> str:
    data_key = value.split("::")[0]
    value_str = "::".join(value.split("::")[1:])

    return DATATYPE_KEY_CAST_MAP[data_key](value_str)
