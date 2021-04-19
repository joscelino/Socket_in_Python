import os
import socket
import sys

sys.path.append(r"D:\Python\Socket")
from logger import logger # NOQA
from server_address.ipaddress import server_address  # NOQA

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

DELETE: bool = False
ERROR = bytes('Error'.encode())

try:
    client.connect(server_address)
except ConnectionRefusedError as e:
    print(f'Connection refused. Please check the server/port: {server_address}!')
    logger.warning(f'Error: {e}')
    sys.exit()

print('Connected!\n')

FILE_NAME = str(input('File >>'))

client.send(FILE_NAME.encode())

with open(FILE_NAME, 'wb') as f:

    while True:
        data = client.recv(1000000)

        if not data:
            break

        if data != ERROR:
            f.write(data)
            print(f'File: {FILE_NAME} receipt.')

        else:
            print(f'File: {FILE_NAME} FAILED!!!!!')
            logger.warning(f'File: {FILE_NAME} FAILED! ')
            DELETE = True

if DELETE is True:
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        DELETE = False
