from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

# Configurar Redis
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_password = os.getenv("REDIS_PASSWORD", None)

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

@app.route('/')
def home():
    # Incrementar contador de visitas
    visits = r.incr("visitor_count")
    return jsonify({"visits": visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
