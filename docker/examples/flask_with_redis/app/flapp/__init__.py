from flapp.common.utils import format_redis_value, parse_redis_value
from flapp.common.database import connect_redis_instance
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Home page!"


@app.route("/get/<name>")
def get_key(name):
    try:
        redis = connect_redis_instance()
        assert redis is not None, "Could not establish connection to redis."

        value: bytes = redis.get(name=name)
        value: str = value.decode("utf-8")
        value = parse_redis_value(value)
        redis.close()

        return jsonify({
            "operation": "GET",
            "key": name,
            "value": value,
        })
    except Exception as e:
        error_message = f"Error encountered in the operation : {e}"
        print(error_message)
        return error_message, 500


@app.route("/set/<name>/<value>")
def set_key(name, value):
    try:
        redis = connect_redis_instance()
        assert redis is not None, "Could not establish connection to redis."

        value = format_redis_value(value)
        status = redis.set(name=name, value=value)
        redis.close()

        return jsonify({
            "operation": "SET",
            "status": status,
            "key": name,
            "value": value,
        })
    except Exception as e:
        error_message = f"Error encountered in the operation : {e}"
        print(error_message)
        return error_message, 500


if __name__ == "__main__":
    app.run()
