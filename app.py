from flask import Flask, jsonify
from nepse import Nepse

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/nepse")
def get_nepse():
    nepse = Nepse()

    index = nepse.get_index()
    summary = nepse.get_summary()

    return jsonify({
        "index": index,
        "turnover": summary.get("totalTurnover"),
        "trades": summary.get("totalTrades"),
        "shares": summary.get("totalSharesTraded")
    })
