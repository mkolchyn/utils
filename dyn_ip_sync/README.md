# DynIPSync

**DynIPSync** is a lightweight Python application for synchronizing a server's **dynamic public IP address** with a static server.  

It consists of two parts:

- **Server A (Receiver)** → A Flask API that accepts IP updates and stores the latest IP.  
- **Server B (Client)** → A Python client that detects its current public IP and sends updates to Server A when the IP changes.  

This is useful when one server has a **dynamic IP** (e.g., at home, on cloud without elastic IP) and needs to be tracked by another server with a **static IP**.

---

## ✨ Features
- Detects IP changes automatically.  
- Sends updates only when the IP changes (avoids noise).  
- Token-based authentication between servers.  
- Configurable via `.env` files.  
- Dockerized (with `docker-compose`).  
- Persists the last known IP in a mounted volume.  

---

## ⚙️ Configuration

Both services use `.env` files for configuration. Create the file and place it in the root directory: `dyn_ip_sync/.env`.

### Example: **.env**
```env
SERVER_A_URL=http://server_a:5000/update-ip
API_TOKEN=supersecrettoken
CHECK_INTERVAL=300
SERVER_B_IP_FILE_PATH=./server_b/artifact/server_b_last_ip.txt
SERVER_A_IP_FILE_PATH=./server_a/artifact/server_b_last_ip.txt
SERVER_A_HOST=0.0.0.0
SERVER_A_PORT=5000
```

**Server A**
| Variable                | Description |
|-------------------------|-------------|
| SERVER_A_IP_FILE_PATH   | Path where Server A stores the last received IP from Server B. Should be writable by the app. |
| API_TOKEN               | Shared secret token to authenticate requests from Server B. Must match Server B’s API_TOKEN. |
| SERVER_A_HOST           | Host/IP on which the Flask server listens. Use `0.0.0.0` for all interfaces. |
| SERVER_A_PORT           | Port on which the Flask server runs (e.g., `5000`). |

**Server B**
| Variable                | Description |
|-------------------------|-------------|
| SERVER_A_URL            | Full URL of Server A endpoint to send IP updates (e.g., `http://server_a:5000/update-ip`). |
| API_TOKEN               | Shared secret token to authenticate requests to Server A. Must match Server A’s API_TOKEN. |
| CHECK_INTERVAL          | Time interval (in seconds) between consecutive IP checks. Only sends updates if IP changed. |
| SERVER_B_IP_FILE_PATH   | Path to a local file where Server B stores its last known public IP to avoid redundant updates. |


---


## 🐳 Run with Docker

**Build and start Server A:**
```init
docker-compose up --build -d server_a

```
**Build and start Server B:**
```init
docker-compose up --build -d server_b

```


---


## 📌 Roadmap

- Add optional HTTPS via Let’s Encrypt.
- Add `/current-ip` endpoint on Server A for querying the last IP of Server B.
