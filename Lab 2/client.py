import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc

def receive_file():
    channel = grpc.insecure_channel('localhost:6000')
    stub = file_transfer_pb2_grpc.FileTransferStub(channel)
    response = stub.SendFile(file_transfer_pb2.Empty())

    if response.data:
        received_filename = 'received_file.txt'
        with open(received_filename, 'wb') as file:
            file.write(response.data)
        print(f"File saved as {received_filename}.")
    else:
        print("File not found on the server.")

if __name__ == '__main__':
    receive_file()
