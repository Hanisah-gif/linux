#!/bin/bash

echo "SERVER PEFORMANCE"

echo ""
echo "CPU Usage"
top -bn1 | grep "Cpu(s)" | awk '(print 100-$8"%")'

echo""
echo "Memory Usage:"
free -h

echo ""
echo "Disk Usage"
df -h /

echo ""
echo "Top 5 processses by CPU Usage:"
ps aux --sort=-%cpu | head -n 6

echo ""
echo "top 5 Processes by Memory Usage:"
ps aux --sort=-%mem | head -n 6
