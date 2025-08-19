import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SERVER_A_URL = os.getenv("SERVER_A_URL")
# Authentication token 
API_TOKEN = os.getenv("API_TOKEN")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 300))
SERVER_B_IP_FILE_PATH = os.getenv("SERVER_B_IP_FILE_PATH", "./server_b/artifact/server_b_last_ip.txt")
# Where to save the latest IP from Server B
SERVER_A_IP_FILE_PATH = os.getenv("SERVER_A_IP_FILE_PATH", "./server_a/artifact/server_a_last_ip.txt")
# Flask server settings
SERVER_A_HOST = os.getenv("SERVER_A_HOST", "0.0.0.0")
SERVER_A_PORT = int(os.getenv("SERVER_A_PORT", 5000))
# Optional SSL cert/key for HTTPS
SSL_CERT = os.getenv("SSL_CERT", None)
SSL_KEY = os.getenv("SSL_KEY", None)

if not SERVER_A_URL or not API_TOKEN:
    raise ValueError("SERVER_A_URL and API_TOKEN must be set in .env")
