# Utils

## CPU Temperature Logger 
Location: `log_cpu_temp`

A simple Bash script that continuously logs the CPU temperature of your system at regular intervals and keeps a rolling 24-hour log. This project also includes a systemd service configuration to run the logger automatically in the background.

## DynIPSync
Location: `dyn_ip_sync`

**new version**

DynIPSync is a lightweight Python application that monitors your machine’s public IP address and notifies all Telegram subscribers whenever it changes. Users can subscribe/unsubscribe directly via the Telegram bot, and also query the last known IP.

**old version** ([link](https://github.com/mkolchyn/utils/tree/814255be1782defc3b715400d96bdf5c0a5f4d10))

DynIPSync is a lightweight Python application for synchronizing a server's dynamic public IP address with a static server.
