
import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "CENG413 HW-2 App")
PORT = int(os.getenv("PORT", "8080"))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
COUNTER_KEY = os.getenv("COUNTER_KEY", "hw2:counter")

redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    socket_connect_timeout=3,
    socket_timeout=3,
)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to my Docker Compose application!",
        "application": APP_NAME,
        "endpoints": [
            "/health",
            "/info",
            "/count",
            "/count/increment"
        ]
    })


@app.route("/health")
def health():
    try:
        redis_client.ping()
        return jsonify({
            "status": "healthy",
            "redis": "connected"
        }), 200
    except redis.RedisError:
        return jsonify({
            "status": "unhealthy",
            "redis": "disconnected"
        }), 503


@app.route("/info")
def info():
    return jsonify({
        "application": APP_NAME,
        "redis_host": REDIS_HOST,
        "redis_port": REDIS_PORT
    })


@app.route("/count", methods=["GET"])
def get_count():
    count = redis_client.get(COUNTER_KEY)
    return jsonify({"count": int(count or 0)})


@app.route("/count/increment", methods=["POST"])
def increment_count():
    count = redis_client.incr(COUNTER_KEY)
    return jsonify({"count": count})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
