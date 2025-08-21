from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ip", methods=["GET"])
def get_ip():
    """
    Returns the client's IP address in JSON.
    Works behind proxies (Render, Vercel, Cloudflare) using X-Forwarded-For.
    """
    # Check for X-Forwarded-For header first (proxy)
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip = request.remote_addr  # fallback

    return jsonify({
        "ip": ip,
        "note": "Fetched client IP address"
    })

if __name__ == "__main__":
    # Local testing
    app.run(host="0.0.0.0", port=5000)
