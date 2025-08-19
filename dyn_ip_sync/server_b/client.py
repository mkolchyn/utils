import time
from shared import config, utils

def main():
    print("[*] DynIPSync client started.")
    while True:
        current_ip = utils.get_public_ip()
        if current_ip:
            last_ip = utils.read_last_ip(config.SERVER_B_IP_FILE_PATH)
            if current_ip != last_ip:
                utils.write_last_ip(config.SERVER_B_IP_FILE_PATH, current_ip)
                utils.send_ip_to_server(current_ip)
            else:
                print(f"[-] IP unchanged ({current_ip}), not sending.")
        time.sleep(config.CHECK_INTERVAL)

if __name__ == "__main__":
    main()
