import os
import socket
import sys

sys.path.append(r"D:\Python\Socket")
from logger import logger # NOQA
from server_address.ipaddress import server_address  # NOQA

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen(1)

connection, address = server.accept()
ERROR = bytes('Error'.encode())

FILE_NAME = connection.recv(1024).decode()

if os.path.exists(FILE_NAME) is False:
    print(f'File {FILE_NAME} was not found.')
    logger.warning(f'File: {FILE_NAME} was not found! ')
    connection.send(ERROR)
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    sys.exit()

else:
    with open(FILE_NAME, 'rb') as f:
        for data in f.readlines():
            connection.send(data)

            print(f'File: {FILE_NAME} sent.')
