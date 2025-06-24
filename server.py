import socket

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Ouvindo na porta: {PORT}")

    try:
        connection, addrs = server.accept()
        print(f"Conexão de {addrs} aceita")
        with connection:
            with open('file.txt', 'wb') as file:
                while True:
                    data = connection.recv(1024)
                    if not data:
                        break
                    file.write(data)

    except ConnectionError:
        print("Erro de conexão")


