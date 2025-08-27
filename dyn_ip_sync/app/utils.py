import os
import requests
import json
import config

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

def load_subscribers():
    if os.path.exists(config.SUB_FILE_PATH):
        with open(config.SUB_FILE_PATH) as f:
            return set(json.load(f))
    return set()

def save_subscribers(subscribers):
    with open(config.SUB_FILE_PATH, "w") as f:
        json.dump(list(subscribers), f)

def add_subscriber(chat_id, subscribers):
    subscribers.add(chat_id)
    save_subscribers(subscribers)

def remove_subscriber(chat_id, subscribers):
    subscribers.discard(chat_id)
    save_subscribers(subscribers)

def send_telegram_message(message, chat_id):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, json=payload, timeout=10)
    except requests.RequestException as e:
        print(f"Failed to send message to {chat_id}: {e}")

def broadcast(message, subscribers):
    for chat_id in subscribers:
        send_telegram_message(message, chat_id)

def handle_updates(subscribers, last_update_id=None):
    url = f"https://api.telegram.org/bot{config.TELEGRAM_TOKEN}/getUpdates"
    if last_update_id:
        url += f"?offset={last_update_id + 1}"

    try:
        r = requests.get(url, timeout=10).json()
    except Exception:
        return last_update_id

    for result in r.get("result", []):
        update_id = result["update_id"]
        chat_id = result["message"]["chat"]["id"]
        text = result["message"].get("text", "")

        if text == "/start":
            add_subscriber(chat_id, subscribers)
            send_telegram_message("Subscribed to IP updates ✅", chat_id)
        elif text == "/stop":
            remove_subscriber(chat_id, subscribers)
            send_telegram_message("Unsubscribed from IP updates ❌", chat_id)

        last_update_id = update_id

    return last_update_id