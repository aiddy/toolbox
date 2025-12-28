#!/bin/bash
# route_4g.sh -- Configure default route for 4G network which is on eth0 on pi 
#!/bin/bash
# route_4g.sh

# Delete only default routes, not local network routes
sudo ip route del default 2>/dev/null || true

# Ensure local network routes exist first
sudo ip route add 192.168.0.0/24 dev wlan0 proto kernel scope link src 192.168.0.187 2>/dev/null || true
sudo ip route add 192.168.168.0/24 dev eth0 proto kernel scope link src 192.168.168.100 2>/dev/null || true

# NOW add default route (gateway is reachable now)
sudo ip route add default via 192.168.168.1 dev eth0 metric 100

# Flush conntrack
echo 1 | sudo tee /proc/sys/net/netfilter/nf_conntrack_max > /dev/null 2>&1
sleep 1
echo 65536 | sudo tee /proc/sys/net/netfilter/nf_conntrack_max > /dev/null 2>&1

echo "Routes set to 4G (cellular):"
ip route show
echo ""
echo "Restart Xbox network connection for changes to take effect"
