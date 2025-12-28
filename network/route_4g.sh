#!/bin/bash
# route_4g.sh -- Configure default route for 4G network which is on eth0 on pi 
sudo ip route del default
sudo ip route add default via 192.168.168.1 dev eth0