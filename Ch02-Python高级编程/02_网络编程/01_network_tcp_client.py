import socket


def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect("127.0.0.1", 8080)
    send_data = "client...".encode("utf-8")
    tcp_client_socket.send(send_data)

    recv_data = tcp_client_socket.recv(1024)

    print(recv_data)
    print(recv_data.decode("utf-8"))

    tcp_client_socket.close()
