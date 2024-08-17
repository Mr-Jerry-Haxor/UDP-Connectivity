# UDP-Connectivity
This project is AIm to establish a  connectivity between Raspberry and Android Mobile app
# Raspberry Pi IP Broadcast on Boot

The code automates the broadcasting of the Raspberry Pi's IP address on boot using a Python script. It utilizes UDP broadcasting to send the IP address to all devices on the same network segment.

## Requirements

- Raspberry Pi running Raspbian or similar Linux distribution
- Python 3.x installed on the Raspberry Pi
- Basic understanding of Linux and Python scripting

## Installation

### Clone the Repository

```bash
git clone https://github.com/Mr-Jerry-Haxor/UDP-Connectivity.git
```
```
cd UDP-Connectivity

sudo cp broadcast_ip.py /opt/broadcast_ip.py
```

## Make it executable:
```
sudo chmod +x /opt/broadcast_ip.py
```

Create a new service file
```
sudo nano /etc/systemd/system/broadcast_ip.service
```


Paste the following content into the file

```
[Unit]
Description=Custom broadcast ip Service
After=network.target

[Service]
Type=simple
ExecStart=sudo /usr/bin/python3 /opt/broadcast_ip.py > /tmp/broadcast_ip.log 2>&1 &
Restart=always
RestartSec=3
User=root   
Group=root  

[Install]
WantedBy=multi-user.target
```

save and close the file by pressing CTRL + X, then Y to confirm the changes, and Enter to exit.


Reload systemd and Start the Service
After creating the service file, reload systemd to read the new service file and start the service:

```
sudo systemctl daemon-reload

sudo systemctl start broadcast_ip
```

Enable the Service to Start on Boot

```
sudo systemctl enable broadcast_ip
```

Check the Status
You can check the status of your service to ensure it's running without errors:

```
sudo systemctl status broadcast_ip
```




Usage

Run on Boot: The Python script (broadcast_ip.py) runs automatically on Raspberry Pi boot. It broadcasts the Raspberry Pi's IP address every 3 seconds.
Logs: Check the log file (/tmp/broadcast_ip.log) to verify the script's operation and to see the IP address broadcasts.


### Download the Apk from HERE 
https://github.com/Mr-Jerry-Haxor/UDP-Connectivity/releases/download/v1/UDPListener.apk

This Apk file Helps to listen the UDP Broadcast Message from UDP sender device , ( Default port : 5005 ) 

Troubleshooting

If the script does not start on boot, check crontab setup and permissions (chmod +x).
Ensure Python 3.x is installed and accessible.
Verify network connectivity and firewall settings if broadcasts are not received on other devices.

