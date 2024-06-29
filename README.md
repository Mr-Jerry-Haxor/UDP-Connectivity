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
```

## Make it executable:
```
chmod +x broadcast_ip.py
```

## get the path of the file 
```
pwd
```
By excuting you will get the past of the current diretory, copy it to use in next steps.

## adding script to run on system Boot
```
crontab -e
```

Add the following line to crontab:

```
@reboot <paste_copied_path>/broadcast_ip.py > /tmp/broadcast_ip.log 2>&1 &
```

Save and exit the editor


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

