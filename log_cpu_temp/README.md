# CPU Temperature Logger

A simple Bash script that continuously logs the CPU temperature of your system at regular intervals and keeps a rolling 24-hour log. This project also includes a systemd service configuration to run the logger automatically in the background.

---

## Features

- Logs CPU core temperatures to a CSV file.
- Timestamped entries for easy tracking.
- Maintains a rolling 24-hour log, automatically removing older data.
- Configurable sampling interval.
- Can run as a systemd service for automatic startup and background operation.

---

## Prerequisites

- Linux system with `sensors` command installed (from `lm-sensors` package).
- Bash shell.
- Systemd (for service setup).
- `awk`, `grep`, `tr`, and `xargs` utilities (usually available by default on most Linux distributions).

Install `lm-sensors` if not already installed:

```bash
sudo apt install lm-sensors    # Debian/Ubuntu
sudo yum install lm_sensors    # RHEL/CentOS
sudo pacman -S lm_sensors      # Arch
```

Then, detect available sensors:
```bash
sudo sensors-detect
```
---

## Installation

Clone or download this repository.
Make the script executable:
```bash
chmod +x log_cpu_temp.sh
```

Place the script in a desired directory, e.g., `/home/username/.`

---

## Usage

Run the script manually:
```bash
./log_cpu_temp.sh
```

The script will create a log file named: `cpu_temp_YYYY-MM-DD_HH-MM.log`

The first row contains headers: `Timestamp, Core0, Core1`.
Subsequent rows contain timestamps and corresponding CPU temperatures for each core.
Logs older than 24 hours are automatically removed.

You can configure:
- `INTERVAL` – seconds between temperature samples (default: 30s)
- `RETENTION` – how long to keep logs (default: 24 hours)

---

## Systemd Service Setup

To run the logger automatically in the background, you can set up a systemd service.
1. Create the service file `/etc/systemd/system/cpu_logger.service`:
```init
[Unit]
Description=CPU Temperature Logger
After=network.target

[Service]
Type=simple
ExecStart=/home/username/log_cpu_temp.sh
Restart=always
User=username
WorkingDirectory=/home/username

[Install]
WantedBy=multi-user.target
```

2. Reload systemd to recognize the new service:
```bash
sudo systemctl daemon-reload
```

3. Enable the service to start at boot:
```bash
sudo systemctl enable cpu_logger.service
```

4. Start the service:
```bash
sudo systemctl start cpu_logger.service
```

5. Check the service status:
```bash
sudo systemctl status cpu_logger.service
```

---

## Log Format

The CSV log file has the following structure:
```csv
Timestamp, Core0, Core1
2025-08-20 12:00:00, 42, 44
2025-08-20 12:00:30, 43, 45
...
```

---

## Notes
- Make sure your user has permissions to read CPU temperature sensors.
- Modify the ExecStart path in the service file according to your script’s location.
- The script assumes two CPU cores (Core0 and Core1). Modify the grep/awk command in the script if your CPU has more cores.
