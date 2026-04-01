from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/data")
def get_data():
	time.sleep(0.1)
	return jsonify({"message": "Hello from RHEL backend!"})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001)
