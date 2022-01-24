import socket

from view import index, blog, info, user, error_404


# Словарь со всеми маршрутами. В ключе маршрут, в значении вьюха, которая его обрабатывает
URLS = {
    '/': index,
    '/blog': blog,
    '/info': info,
    '/user': user
}


def parse_request(request: str) -> tuple[str, str]:
    """
    Функция, которая парсит клиентский запрос.

    Парсит метод запроса и url, на который обратился клиент.
    """
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method: str, url: str) -> tuple[str, int]:
    """
    Функция, генерирующая заголовок пакета, чтобы браузер понимал ответ сервера.
    """
    if method != 'GET':
        return 'HTTP/1.1 405 Method now allowed\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404
    return 'HTTP/1.1 200 OK\n\n', 200
    # Эта закоммментированная часть кода - полный аналог if'ов, но с приминением
    # новой фишки питона версии 3.10 - оператора match/case.
    # match method:
    #     case 'GET':
    #         if url not in URLS:
    #             return 'HTTP/1.1 404 Not found\n\n', 404
    #         return 'HTTP/1.1 200 OK\n\n', 200
    #     case _:
    #         return 'HTTP/1.1 405 Method now allowed\n\n', 405


def generate_content(status_code: int, url: str) -> str:
    """
    Функция, добавляющая в ответ тело, полезную информацию, то, что предназначено
    для пользователя. В нашем случае - это html разметка, чтобы браузер отобразил её
    в виде кнопок, текстов, картинок и тд.

    Сначала происходит обработка ошибок:
    404 - пользователь обратился на несуществующий ресурс;
    405 - пользователь послал неразрешенный HTTP запрос (всё, кроме GET в нашем проекте);
    см. строку 29 и вот эта ссылка (обязательно):
    https://www.youtube.com/watch?v=RlccXUx4LVw

    Если ни одно из условий не выполняется, тогда получаем из словаря по ключу вьюху и
    вызываем её.
    """
    if status_code == 404:
        return error_404()
    elif status_code == 405:
        return '<h1>405</h1><h3>Method not allowed</h3>'
    return URLS[url]()


def generate_response(request: str) -> bytes:
    """
    Функция, которая генерирует ответ для клиента.

    Генерация ответа состоит из трёх этапов:
    1. Парсинг запроса, откуда нужно получить HTTP-метод и url, на который обратился клиент;
    2. Генерация заголовка для браузера, чтобы он правильно понимал ответ нашего сервера, а так
    же генерация статус кода, от которого зависит сценарий ответа клиенту (либо всё хорошо, либо плохо);
    3. Генерация тела ответа, которое представляет собой строку из HTML документа.

    На выходе функция отдаёт заголовки ответа + тело в байтовом представлении.
    """
    method, url = parse_request(request)  # парсинг запроса
    headers, status_code = generate_headers(method, url)  # генерация заголовка для браузера
    body = generate_content(status_code, url)  # генерация тела ответа
    return (headers + body).encode()


def run():
    """
    Главная функция, которая запускает сервер на адресе localhost и порту 5000.
    """
    # Тут настраиваем наш сервер
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # В этом цикле происходит работа с клиентом
    while True:
        # Получение подключение клиента, чтение его запроса и печать в консоль
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(f'Клиент: {addr} -> \n{request.decode("utf-8")}\n')

        # Здесь гененрируется ответ на пользовательский запрос
        response = generate_response(request.decode())

        # Здесь отсылаем клиенту ответ и закрываем с ним соединение
        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    run()
