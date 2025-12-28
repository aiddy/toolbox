#!/bin/bash
# route_broadband.sh -- Configure default route for broadband network which is on wlan0 on pi 
sudo ip route del default
sudo ip route add default via 192.168.0.1 dev wlan0