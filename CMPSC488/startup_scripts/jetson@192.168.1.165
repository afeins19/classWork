#!/bin/bash

# Sysinfo
neofetch 

# Get boot time
echo "Boot time:"
uptime -s

# Check storage space
echo -e "\nStorage space:"
df -h /

# Check Wi-Fi connection status
echo -e "\nWi-Fi connection status:"
nmcli -t -f DEVICE,STATE,CONNECTION d | grep wifi

# Check if SSH is running
echo -e "\nSSH status:"
systemctl is-active ssh.service

# ------------------------- Packages -------------------------

# Get Python Version 
echo -e "\nChecking Packages..."

echo -e "\nPython:"
python --version 

# Get Pip Version 
pip3.7 --version 

# Check OpenCV version
echo -e "\nOpenCV version:"
python3 -c "import cv2; print(cv2.__version__)" || echo "OpenCV is not installed."

# Check ROS-Melodic version
echo -e "\nROS-Melodic version:"
if [ -n "$(which rosversion)" ]; then
    rosversion -d || echo "ROS-Melodic is not installed."
else
    echo "ROS-Melodic is not installed."
fi

