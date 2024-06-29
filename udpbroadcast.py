#!/usr/bin/env python3

import socket
import time
import subprocess

def get_ip_address():
    # Use subprocess to get the IP address of the Raspberry Pi
    result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
    ip_address = result.stdout.strip()
    return ip_address

def broadcast_ip(ip_address, port):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Broadcast address
    broadcast_address = '<broadcast>'
    
    # Construct the message to broadcast
    message = f"Raspberry Pi IP: {ip_address}".encode()
    
    try:
        while True:
            sock.sendto(message, (broadcast_address, port))
            print(f"Broadcasted: {message.decode()} to {broadcast_address}:{port}")
            time.sleep(3)  # Broadcast every 3 seconds
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()

if __name__ == "__main__":
    # Get the IP address of the Raspberry Pi
    ip_address = get_ip_address()
    
    # Port for broadcasting (choose an unused port)
    broadcast_port = 5005
    
    # Broadcast the IP address
    broadcast_ip(ip_address, broadcast_port)
