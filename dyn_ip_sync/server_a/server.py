from flask import Flask, request, abort
import os
from shared import config

app = Flask(__name__)

@app.route("/update-ip", methods=["POST"])
def update_ip():
    # Check token in Authorization header
    token = request.headers.get("Authorization")
    if token != f"Bearer {config.API_TOKEN}":
        abort(403)  # Forbidden

    ip = request.form.get("ip")
    if ip:
        previous_ip = None
        if os.path.exists(config.SERVER_A_IP_FILE_PATH):
            with open(config.SERVER_A_IP_FILE_PATH, "r") as f:
                previous_ip = f.read().strip()

        if ip != previous_ip:
            """Write current IP to file, creating directories if needed"""
            os.makedirs(os.path.dirname(config.SERVER_A_IP_FILE_PATH), exist_ok=True)
            with open(config.SERVER_A_IP_FILE_PATH, "w") as f:
                f.write(ip)
            print(f"[+] IP updated: {ip}")
        else:
            print(f"[-] No change, IP still: {ip}")

        return "IP received", 200

    return "No IP provided", 400


if __name__ == "__main__":
    ssl_context = (config.SSL_CERT, config.SSL_KEY) if config.SSL_CERT and config.SSL_KEY else None
    app.run(host=config.SERVER_A_HOST, port=config.SERVER_A_PORT, ssl_context=ssl_context)
