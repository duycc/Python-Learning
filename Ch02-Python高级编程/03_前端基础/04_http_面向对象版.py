# -*- coding: utf-8 -*-
"""
 * @file     04_http_面向对象版.py
 * @brief    
 * @author   YongDu
 * @date     2022-09-24
"""

import socket
import threading


class HttpWebServer:
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 9000))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(client_socket):
        recv_client_data = client_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("Browser have closed")
            return

        recv_client_data = recv_client_data.decode("utf-8")
        print(recv_client_data)

        request_list = recv_client_data.split(" ", maxsplit=2)
        request_path = request_list[1]
        print("request_path={}".format(request_path))

        if request_path == "/":
            request_path = "/index.html"
        try:
            with open("./static" + request_path, "rb") as f:
                file_data = f.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: PWS1.0\r\n"
            with open("./static/error.html", "rb") as f:
                file_data = f.read()
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            client_socket.send(response_data)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWS1.0\r\n"
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            client_socket.send(response_data)
        finally:
            client_socket.close()

    def start(self):
        while True:
            client_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(client_socket,))
            sub_thread.setDaemon(True)  # 设置守护主线程，防止主线程无法退出
            sub_thread.start()


def main():
    web_server = HttpWebServer()
    web_server.start()


if __name__ == "__main__":
    main()
