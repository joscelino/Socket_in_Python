import os
import socket
import sys
sys.path.append(r"D:\Python\Socket")
from server_address.ipaddress import server_address


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
delete = False

try:
    client.connect(server_address)
except ConnectionRefusedError:
    print(f'Connection refused. Please check the server/port: {server_address}!')
    exit()

print('Connected!\n')

file_name = str(input('File >>'))

client.send(file_name.encode())

with open(file_name, 'wb') as f:

    while True:
        data = client.recv(1000000)

        if not data:
            break

        elif data != bytes('Error'.encode()):
            f.write(data)
            print(f'File: {file_name} receipt.')

        else:
            print(f'File: {file_name} FAILED!!!!!')
            delete = True

if delete is True:
    if os.path.exists(file_name):
        os.remove(file_name)
        delete = False
