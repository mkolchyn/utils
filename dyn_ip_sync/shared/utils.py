import os
import requests
from shared import config

def get_public_ip():
    """Fetch current public IP"""
    try:
        return requests.get("https://api.ipify.org", timeout=5).text.strip()
    except Exception as e:
        print(f"[!] Failed to fetch public IP: {e}")
        return None

def read_last_ip(filepath):
    """Read last stored IP"""
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read().strip()
    return None

def write_last_ip(filepath, ip):
    """Write current IP to file, creating directories if needed"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(ip)
    print(f"[+] Write last IP ({ip}) to file completed.")

def send_ip_to_server(ip):
    """Send current IP to Server A"""
    try:
        headers = {"Authorization": f"Bearer {config.API_TOKEN}"}
        response = requests.post(
            config.SERVER_A_URL,
            data={"ip": ip},
            headers=headers,
            timeout=5
        )
        print(f"[+] Sent IP {ip}, server response: {response.text}")
    except Exception as e:
        print(f"[!] Failed to send IP: {e}")