import socket
from views import *
from threading import Thread

URLS = {
    '/': index,
    '/article': article
}


def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    return headers + generate_body(url, code)


def generate_headers(method, url):
    if method != 'GET':
        return 'HTTP/1.1 405 Method not allowed\n\n', 405
    if url not in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404

    return 'HTTP/1.1 200 OK\n\n', 200


def generate_body(url, code):
    if code == 404:
        return '<h>404</h><p>Not found</p>'
    if code == 405:
        return '<h>405</h><p>Method not allowed</p>'

    return URLS[url]()


def parse_request(request):
    """Gets method and url out of request."""
    method, url = request.split(' ')[0], request.split(' ')[1]
    return method, url


def run():
    # first initiate server-side socket instance, with IPv4 and TCP protocols
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # then bind it to real IP and PORT
    server_socket.bind(('127.0.0.1', 5000))
    # enable server to accept connections
    server_socket.listen()

    def cycle():
        while True:
            # wait for incoming connection
            client_socket, client_addr = server_socket.accept()
            request = client_socket.recv(1024)
            response = generate_response(request.decode('utf-8'))
            client_socket.sendall(response.encode())
            client_socket.close()

    t1 = Thread(target=cycle)
    t2 = Thread(target=cycle)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    run()
