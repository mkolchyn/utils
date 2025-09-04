import time
import threading
import utils
import config

subscribers = utils.load_subscribers()

# Telegram polling thread
def telegram_polling(subscribers):
    last_update_id = None
    while True:
        last_update_id = utils.handle_updates(subscribers, last_update_id)
        time.sleep(config.TELEGRAM_POLL_INTERVAL)  # poll every <<<TELEGRAM_POLL_INTERVAL>>> seconds for user commands

# IP check thread
def ip_monitor(subscribers):
    while True:
        current_ip = utils.get_public_ip()
        if current_ip:
            last_ip = utils.read_last_ip(config.SERVER_B_IP_FILE_PATH)
            if current_ip != last_ip:
                utils.write_last_ip(config.SERVER_B_IP_FILE_PATH, current_ip)
                message = f"IP changed: {last_ip} → {current_ip}"
                print(f"[+] {message}")
                utils.broadcast(message, subscribers)
            else:
                print(f"[-] IP unchanged ({current_ip}), not sending.")
        time.sleep(config.CHECK_INTERVAL)

def main():
    print("[*] DynIPSync client started.")
    
    # Start Telegram polling in a separate thread
    t1 = threading.Thread(target=telegram_polling, args=(subscribers,), daemon=True)
    t1.start()
    
    # Start IP monitor in the main thread
    ip_monitor(subscribers)

if __name__ == "__main__":
    main()
