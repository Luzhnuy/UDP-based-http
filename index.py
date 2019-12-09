import socket

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 8000))
    accept_data(server_socket)


def accept_data(server_socket):
    print("accept process start")
    request, addr = server_socket.recvfrom(4024)
    parse(addr, server_socket)


def parse(addr, server_socket):
    server_socket.send("h".encode(), addr[1])


if __name__ == "__main__":
    server()