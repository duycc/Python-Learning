# -*- coding: utf-8 -*-
"""
 * @file     web.py
 * @brief    
 * @author   YongDu
 * @date     2022-10-01
"""


import socket
import threading
import sys


import framework


class HttpWebServer:
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(client_socket):
        recv_client_data = client_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("Browser have closed")
            client_socket.close()
            return

        recv_client_data = recv_client_data.decode("utf-8")
        print(recv_client_data)

        request_list = recv_client_data.split(" ", maxsplit=2)
        request_path = request_list[1]
        print("request_path={}".format(request_path))

        if request_path == "/":
            request_path = "/index.html"

        if request_path.endswith(".html"):
            env = {
                "request_path": request_path,
            }
            status, headers, response_body = framework.handle_request(env)
            response_line = "HTTP/1.1 {}\r\n".format(status)
            response_header = ""
            for header in headers:
                response_header += "%s: %s\r\n" % header
            response_data = (response_line + response_header + "\r\n" + response_body).encode("utf-8")
            client_socket.send(response_data)
            client_socket.close()
        else:
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
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python3 xxx.py 8000")
        return
    if not sys.argv[1].isdigit():
        print("Usage: python3 xxx.py 8000")
        return
    port = int(sys.argv[1])
    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == "__main__":
    main()
