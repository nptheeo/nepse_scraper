from flask import Flask, jsonify
from nepse import Nepse
import time

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/nepse")
def get_nepse():
    try:
        nepse = Nepse()
        index = nepse.get_index()
        summary = nepse.get_summary()
        
        return jsonify({
            "index": index,
            "turnover": summary.get("totalTurnover"),
            "trades": summary.get("totalTrades"),
            "shares": summary.get("totalSharesTraded")
        })
    except Exception as e:
        # Return mock data if NEPSE API fails
        return jsonify({
            "index": 2120.45,
            "turnover": 1456789000,
            "trades": 34567,
            "shares": 5678900,
            "error": str(e),
            "message": "Using mock data - NEPSE API unavailable"
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
