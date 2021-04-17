import os
import socket
import sys

sys.path.append(r"D:\Python\Socket")
from server_address.ipaddress import server_address

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen(1)

connection, address = server.accept()
error = bytes('Error'.encode())

file_name = connection.recv(1024).decode()

if os.path.exists(file_name) is False:
    print(f'File {file_name} was not found.')
    connection.send(error)
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    exit()

else:
    with open(file_name, 'rb') as f:
        for data in f.readlines():
            connection.send(data)

            print(f'File: {file_name} sent.')
