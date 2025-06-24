import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as client:
    try:
        client.connect((HOST, PORT))
        with open('file.txt', 'rb') as file:
            client.sendfile(file)
    except ConnectionRefusedError:
        print('Conexão recusada')
