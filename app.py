from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/nepse")
def get_nepse():
    # Return mock NEPSE data
    return jsonify({
        "index": 2120.45,
        "turnover": 1456789000,
        "trades": 34567,
        "shares": 5678900
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
