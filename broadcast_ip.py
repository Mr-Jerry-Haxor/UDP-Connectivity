#!/usr/bin/env python3

import socket
import time
import subprocess

def get_ip_address():
    result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
    ip_address = result.stdout.strip()
    return ip_address

def broadcast_ip(port):
    # Create a UDP socket for broadcasting
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # Broadcast address
    broadcast_address = '<broadcast>'
    
    # Initial IP address
    ip_address = get_ip_address()
    last_update_time = time.time()
    
    try:
        while True:
            current_time = time.time()
            
            # Update IP address every minute (60 seconds)
            if current_time - last_update_time >= 60:
                ip_address = get_ip_address()
                last_update_time = current_time
            
            # Construct the message to broadcast
            message = f"Raspberry Pi's IP: {ip_address}".encode()
            
            # Send broadcast message
            sock.sendto(message, (broadcast_address, port))
            print(f"Broadcasted: {message.decode()} to {broadcast_address}:{port}")
            
            # Wait for 3 seconds before broadcasting again
            time.sleep(3)
    
    except OSError as e:
        print(f"Error occurred: {e}")
    
    except KeyboardInterrupt:
        print("Broadcasting interrupted.")
    
    finally:
        sock.close()  # Close socket when done

if __name__ == "__main__":
    # Port for broadcasting (choose an unused port)
    broadcast_port = 5005
    
    # Broadcast the IP address
    broadcast_ip(broadcast_port)
