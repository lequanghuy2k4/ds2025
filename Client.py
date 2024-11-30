import socket

def receive_file():
    """Receive file from the server."""
    server_host = '127.0.0.1'  
    server_port = 6000          
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))

    # Specify where to save the received file
    received_filename = 'received_file.txt'
    with open(received_filename, 'wb') as file:
        print("Receiving file...")
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("File transfer complete.")
                break
            file.write(data)

    print(f"File saved as {received_filename}.")
    client_socket.close()

if __name__ == '__main__':
    receive_file()