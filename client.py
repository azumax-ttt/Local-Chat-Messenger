import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print(f"サーバーに接続中: {server_address}")
try:
    sock.connect(server_address)
except socket.error as msg:
    print(f"接続エラー: {msg}")
    sys.exit(1)

try:
    while True:
        message = input("メッセージを入力してください: ")
        if not message:
            break
        sock.sendall(message.encode())
        res = str(sock.recv(32))
        if res:
            print(res)
finally:
    print("接続を閉じます")
    sock.close()
