# DynIPSync

A lightweight Python application that monitors your machine’s public IP address and notifies all Telegram subscribers whenever it changes.
Users can subscribe/unsubscribe directly via the Telegram bot, and also query the last known IP.

This is a new version that replaces the old server A/B sync logic with a Telegram alerting system.

---

## ✨ Features
- Detects public IP changes using ipify.org
- Sends alerts via Telegram bot to all subscribers.
- Subscription model with commands:
  - `/start` → subscribe
  - `/stop` → unsubscribe
  - `/status` → check subscription status
  - `/getipaddr` → request last known IP
- Persists:
  - Last known IP (default: `./app/artifact/server_last_ip.txt`, docker: `./data/server_last_ip.txt`)
  - Subscribers (default: `./app/artifact/subscribers.json`, docker: `./data/subscribers.json`)
- Configurable via `.env` file.
- Runs two threads:
  - IP Monitor → checks IP every `CHECK_INTERVAL` seconds.
  - Telegram Poller → checks Telegram API every `TELEGRAM_POLL_INTERVAL` seconds. 

---

## ⚙️ Configuration

Environment variables (see `.env.example`):
| Variable                 | Description                               | Default                             |
| ------------------------ | ----------------------------------------- | ----------------------------------- |
| `CHECK_INTERVAL`         | Seconds between IP checks                 | `300`                               |
| `SERVER_B_IP_FILE_PATH`  | Path to file storing last known IP        | `./app/artifact/server_last_ip.txt` |
| `TELEGRAM_TOKEN`         | Bot token from BotFather                  | *(required)*                        |
| `TELEGRAM_POLL_INTERVAL` | Interval (seconds) between Telegram polls | `5`                                 |
| `SUB_FILE_PATH`          | File path to save subscribers list        | `./app/artifact/subscribers.json`   |

---

## 🚀 Installation & Usage
You can run dyn_ip_sync in two ways:

🔹 **Option 1: Run without Docker (local installation)**
1. Clone the repo
```bash
git clone https://github.com/mkolchyn/utils.git
cd utils/dyn_ip_sync
```
2. Configure environment
```bash
cp .env.example .env
# edit .env with your TELEGRAM_TOKEN and options
```
3. Install dependencies
```bash
cd app
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
4. Run
```bash
python app/main.py
```

🔹 **Option 2: Run with Docker**
1. Clone the repo
```bash
git clone https://github.com/mkolchyn/utils.git
cd utils/dyn_ip_sync
```
2. Configure environment
```bash
cp .env.example .env
# edit .env with your TELEGRAM_TOKEN and options
```
3. Build & Run
```bash
docker-compose up -d
```
4. Check logs
```bash
docker logs -f dynipsync_telegram
```
Example log output:
```scss
[*] DynIPSync client started.
[-] IP unchanged (203.0.113.5), not sending.
[+] IP changed: 203.0.113.5 → 203.0.113.77
```
---

## 📲 Telegram Bot Commands

| Command      | Action                               |
| ------------ | ------------------------------------ |
| `/start`     | Subscribe to IP change notifications |
| `/stop`      | Unsubscribe from notifications       |
| `/status`    | Check if you’re currently subscribed |
| `/getipaddr` | Get the last recorded IP address     |
