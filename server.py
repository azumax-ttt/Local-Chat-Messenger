import socket
import os
from faker import Faker

fake = Faker()

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'

try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise

print(f"UNIXソケットをバインド: {server_address}")
sock.bind(server_address)

sock.listen(1)

while True:
    print("接続待機中...")
    connection, client_address = sock.accept()
    try:
        print("接続受け入れ:", client_address)
        while True:
            print('おおおおお')
            data = connection.recv(1024)
            if data:
                print("クライアントからのメッセージ:", data.decode())
                response = fake.sentence()
                
                connection.sendall(response.encode())
            else:
                print("クライアントが接続を切断しました")
                break
    finally:
        connection.close()
