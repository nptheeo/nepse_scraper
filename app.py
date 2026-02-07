from flask import Flask, jsonify
try:
    from nepse import Nepse
    NEPSE_AVAILABLE = True
except ImportError:
    NEPSE_AVAILABLE = False
    import socket

app = Flask(__name__)

# Set socket timeout to 15 seconds
socket.setdefaulttimeout(15)

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/nepse")
def get_nepse():
if not NEPSE_AVAILABLE:
        # Return mock data if nepse module not available
        return jsonify({
            "index": 2120.45,
            "turnover": 1456789000,
            "trades": 34567,
            "shares": 5678900
        })
    
    try:
        # Fetch real NEPSE data with timeout
        nepse = Nepse()
        index = nepse.get_index()
        summary = nepse.get_summary()
        
        return jsonify({
            "index": index,
            "turnover": summary.get("totalTurnover"),
            "trades": summary.get("totalTrades"),
            "shares": summary.get("totalSharesTraded")
        })
    except socket.timeout:
        # If NEPSE API times out, return mock data
        return jsonify({
            "index": None,
            "turnover": None,
            "trades": None,
            "shares": None,
            "error": "NEPSE API timeout",
            "message": "Unable to fetch real data - timeout occurred"
        }), 504
    except Exception as e:
        # For any other error, return error message
        return jsonify({
            "index": None,
            "turnover": None,
            "trades": None,
            "shares": None,
            "error": str(type(e).__name__),
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
