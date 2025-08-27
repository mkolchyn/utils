import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))
SERVER_B_IP_FILE_PATH = os.getenv("SERVER_B_IP_FILE_PATH", "./app/artifact/server_last_ip.txt")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_POLL_INTERVAL = int(os.getenv("TELEGRAM_POLL_INTERVAL", 5))
SUB_FILE_PATH = os.getenv("SUB_FILE_PATH", "./app/artifact/subscribers.json")
