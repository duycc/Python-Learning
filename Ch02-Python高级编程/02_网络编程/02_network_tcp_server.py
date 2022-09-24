import socket


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("127.0.0.1", 8989))
    tcp_server_socket.listen(128)
    service_client_socket, ip_port = tcp_server_socket.accept()
    recv_data = service_client_socket.recv(1024)
    recv_data_length = len(recv_data)

    recv_content = recv_data.decode("utf-8")
    print(recv_content, recv_data_length)
    send_data = "server...".encode("utf-8")
    service_client_socket.send(send_data)
    service_client_socket.close()
    tcp_server_socket.close()
