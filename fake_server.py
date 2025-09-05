import socket
import threading
import logging
from datetime import datetime

# === Logging Setup ===
logging.basicConfig(
    filename="connections.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# === Improved Function to Receive One Line ===
def receive_line(sock):
    data = b''
    while True:
        chunk = sock.recv(1)
        if not chunk:  # Connection closed
            break
        if chunk in [b'\n', b'\r']:
            # Read one more byte to check for \r\n
            next_byte = sock.recv(1)
            if next_byte not in [b'\n', b'\r']:
                # Put the byte back if it wasn't part of CRLF
                sock.sendall(next_byte)
            break
        data += chunk
    return data.decode('utf-8', errors='ignore').strip()

# === Handle Each Client Connection ===
def handle_connection(client_socket, client_address):
    logging.info(f"Connection from {client_address} at {datetime.now()}")
    try:
        # Fake SSH banner
        client_socket.sendall(b"SSH-2.0-OpenSSH_7.4\r\n")

        # Prompt for login (use flush)
        client_socket.sendall(b"login: ")
        username = receive_line(client_socket)

        # Prompt for password (use flush)
        client_socket.sendall(b"password: ")
        password = receive_line(client_socket)

        # Log the fake login attempt
        logging.info(f"Login attempt - User: {username}, Pass: {password}, From: {client_address}")

        # Simulate failed login
        client_socket.sendall(b"\r\nLogin Failed\r\n")
    except Exception as e:
        logging.error(f"Error handling connection from {client_address}: {e}")
    finally:
        client_socket.close()

# === Start the Honeypot Server ===
def start_server(host='0.0.0.0', port=4444):
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)
        print(f"[*] Fake Honeypot Server is running on port {port}")

        while True:
            client, addr = server.accept()
            print(f"[!] Connection from {addr}")
            thread = threading.Thread(target=handle_connection, args=(client, addr))
            thread.start()
    except Exception as e:
        print(f"[!] Failed to start server: {e}")

# === Entry Point ===
if __name__ == "__main__":
    start_server()
