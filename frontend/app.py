from flask import Flask, jsonify
import requests
import time
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
RHEL_IP = os.getenv("RHEL_IP")

@app.route("/")
def home():
    try:
        resp = requests.get(f"http://{RHEL_IP}:5001/data", timeout=5)
        return jsonify({
            "frontend": "ok",
            "backend_response": resp.json(),
            "timestamp": time.time()
        })
    except Exception as e:
        return jsonify({
            "frontend": "error",
            "message": "Backend unreachable",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
