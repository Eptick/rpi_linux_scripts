#!/bin/bash
# The Script
ip=$(hostname -I)
ssid=$(iwgetid -r)
mac=$(cat /sys/class/net/wlan0/address)
cat <<- _EOF_
$ip
$ssid
$mac
_EOF_
curl --data "ip=$ip&ssid=$ssid&mac=$mac" raspberry-dns.herokuapp.com >> /home/pi/Desktop/log
 
