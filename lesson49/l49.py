# Сетевое программирование
import socket


def generate_response(request: str) -> bytes:
    pass


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen() # localhost:5000

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f"Клиент: {addr} -> \n{request.decode()} \n")

        response = generate_response(request.decode())

        client_socket.sendall(response)
        client_socket.close()



if __name__ == "__main__":
    run()


