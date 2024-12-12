import grpc
import file_transfer_pb2
import file_transfer_pb2_grpc
from concurrent import futures
import os

class FileTransferServicer(file_transfer_pb2_grpc.FileTransferServicer):
    def SendFile(self, request, context):
        file_to_send = r'D:\DS\task2\tranfer_file.txt'
        if os.path.exists(file_to_send):
            with open(file_to_send, 'rb') as file:
                return file_transfer_pb2.FileChunk(data=file.read(), filename='transfer_file.txt')
        else:
            context.set_details("File not found.")
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return file_transfer_pb2.FileChunk()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    file_transfer_pb2_grpc.add_FileTransferServicer_to_server(FileTransferServicer(), server)
    server.add_insecure_port('[::]:6000')
    print("Server listening on port 6000...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
