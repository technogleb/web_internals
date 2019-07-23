import socket


def run():
    # first initiate server-side socket instance, with IPv4 and TCP protocols
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # then bing it to real IP and PORT
    server_socket.bind(('localhost', 5000))
    # enable server to accept connections
    server_socket.listen()

    while True:
        # allow accept incoming connections
        client_socket, client_addr = server_socket.accept()
        print(client_socket, client_addr)
        request = client_socket.recv(1024)
        print(request)
        client_socket.sendall('hello'.encode())
        client_socket.close()


if __name__ == "__main__":
    run()
