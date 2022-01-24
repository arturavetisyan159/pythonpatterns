# Сетевое программирование
import socket
from view import index, blog


URLS = {
    '/': index,
    '/blog': blog
}

def parse_request(request: str):
    parsed = request.split(" ")
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method: str, url: str):
    if method != "GET":
        return "HTTP/1.1 405 Method not allowed!\n\n", 405
    if url not in URLS:
        return "HTTP/1.1 404 Not found!\n\n", 404
    return "HTTP/1.1 200 OK!\n\n", 200


def generate_content(code: int, url: str) -> str:
    if code == 404:
        return '<h1>404</h1><h3>Not found</h3>'
    elif code == 405:
        return '<h1>405</h1><h3>Method not allowed</h3>'
    return URLS[url]()


def generate_response(request: str) -> bytes:
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen() # localhost:5000

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f"Клиент: {addr} -> \n{request.decode()}\n")

        response = generate_response(request.decode())

        client_socket.sendall(response)
        client_socket.close()



if __name__ == "__main__":
    run()


