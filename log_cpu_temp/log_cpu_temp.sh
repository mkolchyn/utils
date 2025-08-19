#!/bin/bash

LOGFILE="cpu_temp_$(date +"%Y-%m-%d_%H-%M").log"
INTERVAL=30                # seconds between samples
RETENTION=$((24*60*60))   # 24 hours in seconds

echo "Timestamp, Core0, Core1" > $LOGFILE

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    TEMPS=$(sensors | grep "Core" | awk '{print $3}' | tr -d '+°C' | xargs | tr ' ' ',')
    echo "$TIMESTAMP, $TEMPS" >> $LOGFILE

    # Keep only last 24h of logs
    cutoff=$(date -d "@$(( $(date +%s) - $RETENTION ))" +"%Y-%m-%d %H:%M:%S")
    awk -v cutoff="$cutoff" 'NR==1 || $1" "$2 >= cutoff' $LOGFILE > tmpfile && mv tmpfile $LOGFILE

    sleep $INTERVAL
done
