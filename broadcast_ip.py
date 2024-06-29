#!/usr/bin/env python3

import socket
import time
import subprocess


def broadcast_ip(port):
    while True:
        # Create a UDP socket for broadcasting
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
        ip_address = result.stdout.strip()
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        # Broadcast address
        broadcast_address = '<broadcast>'
        
        while True:
            try:
                if not ip_address:
                    break
                # Construct the message to broadcast
                message = f"Raspberry Pi IP: {ip_address}".encode()
                
                # Send broadcast message
                sock.sendto(message, (broadcast_address, port))
                print(f"Broadcasted: {message.decode()} to {broadcast_address}:{port}")
                
                time.sleep(3)  # Broadcast every 3 seconds
            
            except OSError as e:
                print(f"Error occurred: {e}")
                time.sleep(5)
                continue
            except KeyboardInterrupt:
                break  # Exit the loop on Ctrl+C

        sock.close()  # Close socket when done

if __name__ == "__main__":
    # Port for broadcasting (choose an unused port)
    broadcast_port = 5005
    
    # Broadcast the IP address
    broadcast_ip(broadcast_port)
