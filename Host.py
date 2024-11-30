import socket
import os

def handle_client(conn, address):
    print(f"Connected to {address}.")
    file_to_send = r'/media/icebear/Linux/DS/task1/transfer_file.txt'

    if os.path.exists(file_to_send):
        with open(file_to_send, 'rb') as file:
            print("Starting file transfer...")
            while (chunk := file.read(1024)):
                conn.send(chunk)
            print("File transfer complete.")
    else:
        print("File not found.")
        conn.send(b"File not found!")

    conn.close()

def host():
    """Start the server and listen for connections."""
    server_host = '127.0.0.1'  
    server_port = 6000          
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set socket options
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the address and port
    server_socket.bind((server_host, server_port))
    server_socket.listen(1)
    print(f"Server listening on {server_host}:{server_port}...")

    while True:
        # Accept a connection
        conn, address = server_socket.accept()
        handle_client(conn, address)

if __name__ == '__main__':
    host()